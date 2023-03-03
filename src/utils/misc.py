import pandas as pd
from pathlib import Path
import PySimpleGUI as sg

def convert_to_csv(excel_file_path, output_folder, sheet_name, separator, decimal):
    df = pd.read_excel(excel_file_path, sheet_name)
    filename = Path(excel_file_path).stem
    outputfile = Path(output_folder) / f"{filename}.csv"
    df.to_csv(outputfile, sep=separator, decimal=decimal, index=False)
    sg.popup_no_titlebar("Done! :)")

def display_excel_file(excel_file_path, sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name)
    filename = Path(excel_file_path).name
    sg.popup_scrolled(df.dtypes, "=" * 50, df.head(15), title=filename)

def is_valid_path(filepath):
    if filepath and Path(filepath).exists:
        return True
    sg.PopupError("No file Selected!!!")