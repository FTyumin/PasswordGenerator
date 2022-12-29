import PySimpleGUI as sg
import string
import random

def get_random_string(length):
    
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

layout = [[sg.Text('Amount of characters:'), sg.Input()],
          [sg.Button('Ok'), sg.Button('Cancel')],
          [sg.Text('',key='_TEXT_'),]]

window = sg.Window('Input window').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break
    output = values[0]
    input =get_random_string(int(output))
    window['_TEXT_'].Update(input)

window.Close()



