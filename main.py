import PySimpleGUI as sg
import configparser

import re
import os

sg.theme("DarkGrey5")

config = configparser.ConfigParser()
l1 = []
l2 = []
c1 = []
c2 = []


def ini_filter_1(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".ini"):
                l1.append(os.path.join(root, file))
                window["-L1-"].update(l1)


def ini_filter_2(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".ini"):
                l2.append(os.path.join(root, file))
                window["-L2-"].update(l2)


def r_1(file_1):
    c1 = []
    with open(file_1) as file:
        for line in file:
            c1.append(line.rstrip())
            window["-C1-"].update(c1)


def r_2(file_2):
    c2 = []
    with open(file_2) as file:
        for line in file:
            c2.append(line.rstrip())
            window["-C2-"].update(c2)


layout = [
    [sg.Text('Folder 1'),
     sg.InputText('D:/JetBrains', enable_events=True, key="-FOLDER_1-", size=(30, 10)), sg.FolderBrowse(),
     sg.Button('Scan', enable_events=True, key="-SCAN_1-"),
     sg.Text('Folder 2'),
     sg.InputText('D:/JetBrains', enable_events=True, key="-FOLDER_2-", size=(30, 10)), sg.FolderBrowse(),
     sg.Button('Scan', enable_events=True, key="-SCAN_2-", )],
    [[sg.Listbox(l1, size=(90, 10), enable_events=True, key="-L1-"),
      sg.Listbox(l2, size=(90, 10), enable_events=True, key="-L2-")]],
    [sg.Button('Add to Compare', enable_events=True, key="-ADD-")],
    [sg.Text('Selected File 1'), sg.InputText('', enable_events=True, key="-FILE_1-", )],
    [sg.Text('Selected File 2'), sg.InputText('', enable_events=True, key="-FILE_2-", )],
    [sg.Button('Compare', enable_events=True, key="-COMPARE-")],
    [sg.Listbox(c1, size=(90, 30), enable_events=True, key="-C1-", ),
     sg.Listbox(c1, size=(90, 30), enable_events=True, key="-C2-", )],
]

window = sg.Window('INIParser', layout, size=(1300, 900), element_justification='center')

while True:  # The Event Loop
    event, values = window.read()
    f_1 = re.sub(r"[\['\]]", "", str(values['-L1-']))
    f_2 = re.sub(r"[\['\]]", "", str(values['-L2-']))
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == '-SCAN_1-':
        inputPath1 = values['-FOLDER_1-']
        ini_filter_1(inputPath1)
    if event == '-SCAN_2-':
        inputPath2 = values['-FOLDER_2-']
        ini_filter_2(inputPath2)
    if event == '-L1-' and len(values['-L1-']):
        path1 = values['-L1-']  # if a list item is chosen
    if event == '-L2-' and len(values['-L2-']):
        path2 = values['-L2-']  # if a list item is chosen
    if event == '-ADD-':
        window['-FILE_1-'].Update(f_1)
        window['-FILE_2-'].Update(f_2)
    if event == '-COMPARE-':
        r_1(f_1)
        r_2(f_2)
