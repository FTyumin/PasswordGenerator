import PySimpleGUI as sg
import string
import secrets
import pyperclip


def generate_password(pwd_length, option=0):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    option1 = letters + digits
    option2 = letters + special_chars

    pwd = ''
    if option == 0:
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
    elif option == 1:
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(option1))
    elif option == 2:
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(option2))
    elif option == 3:
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(letters))
    return pwd


sg.theme('LightGrey5')

layout = [
    [sg.Text('Length:', font='Helvetica 15', ), sg.Input()],
    [sg.Checkbox('Add digits', key='digit', default=True)],
    [sg.Checkbox('Add symbols', key='char', default=True)],
    [sg.Button('Generate'), sg.Button('Exit')],
    [sg.Text(size=(30, 3), key='-OUTPUT-', font='Helvetica 20')],
    [sg.Button('Copy to Clipboard', visible=False, key='copy_button')]
]

window = sg.Window('Password generator', element_justification='c').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    output = values[0]

    try:
        output = int(values[0])
    except ValueError:
        window['-OUTPUT-'].update("Please enter a valid integer")
        continue

    if event == 'Generate':
        if not values['digit'] and not values['char']:  # letters only
            password = generate_password(output, 3)
        elif values['digit'] and values['char']:
            password = generate_password(output)
        elif ['digit'] and not values['char']:
            password = generate_password(output, 1)
        elif ['char'] and not values['digit']:
            password = generate_password(output, 2)

    window['-OUTPUT-'].update(password)

    # updating the layout to include copy button
    window['copy_button'].update(visible=True)

    # if clipboard button is pressed, password is copied
    if event == 'copy_button':
        pyperclip.copy(password)

window.Close()
