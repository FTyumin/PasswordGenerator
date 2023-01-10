import PySimpleGUI as sg
import string
import secrets
import pyperclip


def generate_password(pwd_length, alphabet):
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd


# function checks how strong is the password
def pass_strength(input_string):
    n = len(input_string)

    # Checking lower alphabet in string
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

    for i in range(n):
        if input_string[i].islower():
            hasLower = True
        if input_string[i].isupper():
            hasUpper = True
        if input_string[i].isdigit():
            hasDigit = True
        if input_string[i] not in normalChars:
            specialChar = True

    # Strength of password
    if (hasLower and hasUpper and
            hasDigit and specialChar and n >= 8):
        return "Strong"

    elif ((hasLower or hasUpper) and
          specialChar and n >= 6):
        return "Moderate"
    else:
        return "Weak"


sg.theme('LightGrey5')

layout = [
    [sg.Text('Length:', font='Helvetica 15', ), sg.Input(key='-INPUT-')],
    [sg.Checkbox('Add digits', key='digit', default=True)],
    [sg.Checkbox('Add symbols', key='char', default=True)],
    [sg.Checkbox('Add lowercase', key='lowercase', default=True)],
    [sg.Checkbox('Add uppercase', key='uppercase', default=True)],
    [sg.Slider(range=(0, 30), default_value=(25, 75), orientation='h', size=(20, 20), key='-SLIDER-')],
    [sg.Button('Generate'), sg.Button('Exit')],
    [sg.Text(size=(30, 3), key='-OUTPUT-', font='Helvetica 20')],
    [sg.Button('Copy to Clipboard', visible=False, size=(30, 3), key='copy_button')],
    [sg.Text("Password strength", visible=False, size=(25, 3), key='-OUTPUT2-', font='Helvetica 15')]
]

window = sg.Window('Password generator', element_justification='c').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    try:
        output = int(values['-INPUT-'])
    except ValueError:
        window['-OUTPUT-'].update("Please enter a valid integer")
        continue

    value = int(values['-INPUT-'])
    window['-SLIDER-'].Update(value)

    selected_characters = []

    if event == 'Generate':
        if values['digit']:
            selected_characters += string.digits
        if values['char']:
            selected_characters += string.punctuation
        if values['lowercase']:
            selected_characters += string.ascii_lowercase
        if values['uppercase']:
            selected_characters += string.ascii_uppercase

        password = generate_password(output, selected_characters)

        # when password is generated, strength of the password is shown
        password_strength = pass_strength(password)
        window['-OUTPUT2-'].update("Password strength: " + password_strength, visible=True)

    window['-OUTPUT-'].update(password)

    # updating the layout to include copy button
    window['copy_button'].update(visible=True)

    # if clipboard button is pressed, password is copied
    if event == 'copy_button':
        pyperclip.copy(password)

window.Close()
