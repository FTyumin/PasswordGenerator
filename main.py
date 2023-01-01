import PySimpleGUI as sg
import string
import random


def get_random_string(length):
    if length=='':
        return "Enter a number"
    else:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str



layout = [
          [sg.Text('Length:',font=('Helvetica 15')), sg.Input()],
          [sg.Checkbox('Add digits')],
          [sg.Button('Generate'), sg.Button('Exit')],
          [sg.Text(size=(30,3), key='-OUTPUT-',font=('Helvetica 20'))],
         ]

window = sg.Window('Password generator',element_justification='c').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    output = values[0]
    if output == '':
        window['-OUTPUT-'].update("Type a number")
    elif not output.isdigit():
        window['-OUTPUT-'].update("Type a number")
    else:
        input = get_random_string(int(output))
        window['-OUTPUT-'].update(input)


window.Close()
