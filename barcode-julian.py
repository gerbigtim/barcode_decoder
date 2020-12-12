"""Module for reading barcodes."""
import pandas as pd
import string


class Decoder():
    """Decode and encode barcodes with csv."""

    def Decoder(this, csv_file):
        """Construct the class."""
        this.df = pd.read_csv(csv_file)

    def _split_barcode(this, barcode):
        """Split the barcode into a dictionary."""
        barcode_dict = {}
        barcode_dict['Marke'] = barcode[:2]
        barcode_dict['Art'] = barcode[2:4]
        barcode_dict['Material'] = barcode[4:6]
        barcode_dict['Groesse'] = barcode[6:8]
        return barcode_dict

    def decode_barcode(this, barcode):
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
            item_dict[key] = this.df.loc[this.df[key+'Code'] == code][key].values[0]
        item_dict['Farbe'] = barcode[8:]
        return item_dict
