"""Module for reading barcodes."""
import pandas as pd
import string


class Decoder:
    """Decode and encode barcodes with csv."""

    def __init__(this, csv_file):
        """Construct the class."""
        this.df = pd.read_csv(csv_file)
        this.keyes = this._get_keyes()

    def _get_keyes(this):
        """Get all named column names."""
        keyes = this.df.columns
        keyes = [key for key in keyes if not key.startswith('Unnamed:')]
        return keyes

    def _split_barcode(this, barcode):
        """Split the barcode into a dictionary."""
        barcode_dict = {}
        for key, index in zip(this.keyes, range(0, 8, 2)):
            barcode_dict[key] = barcode[index:index+2]
        return barcode_dict

    def decode(this, barcode):
        """Decode the barcode."""
        if not isinstance(barcode, str):
            raise TypeError("Barcode must be passed as a string!")
        if len(barcode) != 14:
            raise ValueError("Barcode must be of length 14!")
        if not all(c in string.hexdigits for c in barcode):
            raise ValueError('Barcode contains non hex digits!')
        barcode = barcode.lower()

        barcode_dict = this._split_barcode(barcode)
        item_dict = {}
        for key, code in barcode_dict.items():
            codes_idx = this.df.columns.get_indexer([key]) + 1
            mask = (this.df.iloc[:, codes_idx] == code).iloc[:, 0]
            item_dict[key] = this.df.loc[mask][key].values[0]
        item_dict['Farbe'] = barcode[8:]
        return item_dict
