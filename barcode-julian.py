"""Module for reading barcodes."""
import pandas as pd


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
    barcode_dict['Farbe'] = barcode[8:]
    return barcode_dict


def decode_barcode(barcode):
    """Decode the barcode."""
    barcode_dict = split_barcode(barcode)
    print(barcode_dict)


def main():
    """Execute the main function."""
    decode_data = pd.read_csv('DecodeSheet.csv')
    print(decode_data)

if __name__ == '__main__':
    main()
