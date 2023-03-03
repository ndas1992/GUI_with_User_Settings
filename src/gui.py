import PySimpleGUI as sg
import pandas as pd
from src.utils.misc import convert_to_csv, display_excel_file, is_valid_path

layout = [
    [sg.Text("INPUT FILE:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx*")))],
    [sg.Text("OUTPUT FILE:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Display Excel File"), sg.Button("Convert to CSV")]
]

window = sg.Window("Excel nonu", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event ==  "Convert to CSV":
        if is_valid_path(filepath=values['-IN-']) and is_valid_path(filepath=values['-OUT-']):
            convert_to_csv(
                excel_file_path=values['-IN-'], 
                output_folder=values['-OUT-'], 
                sheet_name='Sheet1', 
                separator='|', 
                decimal='.'
                )
    if event == "Display Excel File":
        if is_valid_path(filepath=values['-IN-']):

            display_excel_file(
                excel_file_path=values['-IN-'], 
                sheet_name='Sheet1'
                            )
    

window.close()