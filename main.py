import PySimpleGUI as sg
import string
import random


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


layout = [[sg.Text('Amount of characters:'), sg.Input()],
          [sg.Button('Generate'), sg.Button('Exit')],
          [sg.Output(size=(30,3), key='-OUTPUT-',font=('Helvetica 20')),]]

window = sg.Window('Password generator').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break
    output = values[0]
    input = get_random_string(int(output))
    window['-OUTPUT-'].update(input)

window.Close()
