"""Module for reading barcodes."""


def split_barcode(barcode):
    """Split the barcode into a dictionary."""
    if not isinstance(barcode, str):
        raise TypeError("Barcode must be passed as a string!")
    if len(barcode) != 14:
        raise ValueError("Barcode must be of length 14!")
    barcode_dict = {}
    barcode_dict['Marke'] = barcode[:2]
    barcode_dict['Art'] = barcode[2:4]
    barcode_dict['Material'] = barcode[4:6]
    barcode_dict['Groesse'] = barcode[6:8]
    barcode_dict['Rest'] = barcode[8:]
    return barcode_dict
