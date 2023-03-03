import PySimpleGUI as sg
from pathlib import Path


if __name__=="__main__":
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True, convert_bools_and_none=True
    )
    theme = settings['GUI']['theme']
    font_family = settings['GUI']['font_family']
    font_size = settings['GUI']['font_size']
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    main_window()