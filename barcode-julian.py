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
    return barcode_dict


def decode_barcode(barcode, df):
    """Decode the barcode."""
    barcode_dict = split_barcode(barcode)
    item_dict = {}
    for key, code in barcode_dict.items():
        item_dict[key] = df.loc[df[key+'Code'] == code][key].values[0]
    item_dict['Farbe'] = barcode[8:]
    return item_dict


def main():
    """Execute the main function."""
    df = pd.read_csv('DecodeSheet.csv')
    print(decode_barcode('00010203ffffff', df))


if __name__ == '__main__':
    main()
