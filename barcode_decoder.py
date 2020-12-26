"""Module for reading barcodes."""
import pandas as pd
import numpy as np
import string
import collections


class Decoder:
    """Decode and encode barcodes with csv."""

    def __init__(self, csv_file):
        """Construct the class."""
        self.df = pd.read_csv(csv_file, sep=';',encoding='cp1252', dtype=str)
        self._color = 'Farbe'
        self._keys = self._get_keys()

    def _get_keys(self):
        """Get all named column names."""
        keys = self.df.columns
        keys = [key for key in keys if not key.startswith('Unnamed:')]
        keys.append(self._color)
        return keys

    def _split_barcode(self, barcode):
        """Split the barcode into a dictionary."""
        barcode_dict = {}
        for key, index in zip(self._keys, range(0, 8, 2)):
            barcode_dict[key] = barcode[index:index+2]
        return barcode_dict

    def decode(self, barcode):
        """Decode the barcode."""
        if not isinstance(barcode, str):
            raise TypeError("Barcode must be passed as a string!")
        if len(barcode) != 14:
            raise ValueError("Barcode must be of length 14!")
        if not all(c in string.hexdigits for c in barcode):
            raise ValueError(f'Barcode "{barcode}" contains non hex digits!')
        barcode = barcode.lower()

        barcode_dict = self._split_barcode(barcode)
        item_dict = {}
        for key, code in barcode_dict.items():
            idx = self.df.columns.get_indexer([key]) + 1
            mask = (self.df.iloc[:, idx] == code).iloc[:, 0]
            try:
                item_dict[key] = self.df.loc[mask][key].values[0]
            except IndexError:
                raise ItemNotFoundError(f'Code "{code}" not found for "{key}"!')
            try:
                assert isinstance(item_dict[key], str)
            except AssertionError:
                raise ItemNotFoundError(f'No item found in column "{key}" for code "{code}"!')
        item_dict[self._color] = barcode[8:]
        return item_dict

    def encode(self, item_dict):
        """Encode dictionary into barcode."""
        if not collections.Counter(item_dict.keys()) == collections.Counter(self._keys):
            raise ValueError("Dictionary contains wrong keys!")
        if not all(c in string.hexdigits for c in item_dict[self._color]):
            raise ValueError(f'Color "{item_dict[self._color]}" contains non hex digits!')
        barcode = ''
        for key in self._keys[:-1]:
            value = item_dict[key]
            idx = self.df.columns.get_indexer([key]) + 1
            try:
                barcode += self.df.loc[self.df[key] == value].iloc[:, idx].values[0][0]
            except IndexError:
                raise ItemNotFoundError(f'Item "{key}:{value}" not found!')
            except TypeError:
                raise ItemNotFoundError(f'No code found for item "{key}:{value}"!')
        barcode += item_dict[self._color].lower()
        return barcode


class ItemNotFoundError(Exception):
    """Throw this if item is not found in dataframe."""

    pass
