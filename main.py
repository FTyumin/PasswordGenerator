import PySimpleGUI as sg
import string
import secrets



def generate_password(pwd_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd



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
        input = generate_password(int(output))
        window['-OUTPUT-'].update(input)


window.Close()
