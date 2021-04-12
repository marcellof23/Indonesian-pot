import PySimpleGUI as sg
import utilities

def loginDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Login'), ],
              [sg.Input(k='EMAIL', enable_events=True)],
              [sg.Input(k='PASSWORD', enable_events=True)],
              [sg.Button('Login'), sg.Button('Register')],
              [sg.Text(size=(20,1), k='ERRORMSG')]]
    window = sg.Window('Login', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    return window

def registerDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Register'), ],
              [sg.Input(k='EMAIL', enable_events=True)],
              [sg.Input(k='PASSWORD', enable_events=True)],
              [sg.Input(k='REPEATEDPASSWORD', enable_events=True)],
              [sg.Input(k='PHONE', enable_events=True)],
              [sg.Input(k='ADDRESS', enable_events=True)],
              [sg.Button('Register'), sg.Button('Login')],
              [sg.Text(size=(20,1),  k='-OUTPUT-')]]
    window = sg.Window('Register', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    utilities.setPlaceholder(window["REPEATEDPASSWORD"], placeholderText="repeat password")
    utilities.setPlaceholder(window["PHONE"], placeholderText="phone number")
    utilities.setPlaceholder(window["ADDRESS"], placeholderText="address")
    return window