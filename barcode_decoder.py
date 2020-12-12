"""Module for reading barcodes."""
import pandas as pd
import string
import collections


class Decoder:
    """Decode and encode barcodes with csv."""

    def __init__(this, csv_file):
        """Construct the class."""
        this.df = pd.read_csv(csv_file)
        this._color = 'Farbe'
        this._keys = this._get_keys()

    def _get_keys(this):
        """Get all named column names."""
        keys = this.df.columns
        keys = [key for key in keys if not key.startswith('Unnamed:')]
        keys.append(this._color)
        return keys

    def _split_barcode(this, barcode):
        """Split the barcode into a dictionary."""
        barcode_dict = {}
        for key, index in zip(this._keys, range(0, 8, 2)):
            barcode_dict[key] = barcode[index:index+2]
        return barcode_dict

    def decode(this, barcode):
        """Decode the barcode."""
        if not isinstance(barcode, str):
            raise TypeError("Barcode must be passed as a string!")
        if len(barcode) != 14:
            raise ValueError("Barcode must be of length 14!")
        if not all(c in string.hexdigits for c in barcode):
            raise ValueError(f'Barcode {barcode} contains non hex digits!')
        barcode = barcode.lower()

        barcode_dict = this._split_barcode(barcode)
        item_dict = {}
        for key, code in barcode_dict.items():
            idx = this.df.columns.get_indexer([key]) + 1
            mask = (this.df.iloc[:, idx] == code).iloc[:, 0]
            item_dict[key] = this.df.loc[mask][key].values[0]
        item_dict[this._color] = barcode[8:]
        return item_dict

    def encode(this, item_dict):
        """Encode dictionary into barcode."""
        if not collections.Counter(item_dict.keys()) == collections.Counter(this._keys):
            raise ValueError("Dictionary contains wrong keys!")
        if not all(c in string.hexdigits for c in item_dict[this._color]):
            raise ValueError(f'Color {item_dict[this._color]} contains non hex digits!')
        barcode = ''
        for key in this._keys[:-1]:
            value = item_dict[key]
            idx = this.df.columns.get_indexer([key]) + 1
            try:
                barcode += this.df.loc[this.df[key] == value].iloc[:, idx].values[0][0]
            except IndexError:
                raise ItemNotFoundError(f'Item {value} not found in column {key}!')
        barcode += item_dict[this._color].lower()
        return barcode


class ItemNotFoundError(Exception):
    """Throw this if item is not found in dataframe."""

    pass
