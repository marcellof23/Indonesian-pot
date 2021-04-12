import PySimpleGUI as sg
from screeninfo import get_monitors

def loginDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Login'), ],
              [sg.Input(k='email', enable_events=True)],
              [sg.Input(k='password', enable_events=True)],
              [sg.Button('Login'), sg.Button('Register')]]

    return sg.Window('Login', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))

def registerDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Register'), ],
              [sg.Input(k='-IN-', enable_events=True)],
              [sg.Text(size=(20,1),  k='-OUTPUT-')],
              [sg.Button('Register'), sg.Button('Login')]]

    return sg.Window('Register', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))