import PySimpleGUI as sg
from screeninfo import get_monitors

monitor = get_monitors()[0]
windowWidth , windowHeight = monitor.width, monitor.height 

def loginDisplay():
    layout = [[sg.Text('Login'), ],
              [sg.Input(k='-IN-', enable_events=True)],
              [sg.Text(size=(20,1),  k='-OUTPUT-')],
              [sg.Button('Login'), sg.Button('Register')]]

    return sg.Window('Login', layout, finalize=True, size= (windowWidth,windowHeight))

def registerDisplay():
    layout = [[sg.Text('Register'), ],
              [sg.Input(k='-IN-', enable_events=True)],
              [sg.Text(size=(20,1),  k='-OUTPUT-')],
              [sg.Button('Next >'), sg.Button('Login')]]

    return sg.Window('Register', layout, finalize=True, size= (windowWidth,windowHeight))