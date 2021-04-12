import style
import PySimpleGUI as sg
import utilities


def loginDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Login',**style.title)],
              [sg.Input(k='EMAIL', enable_events=True)],
              [sg.Input(k='PASSWORD', enable_events=True)],
              [sg.Button('Login',**style.bl), sg.Button('Register',**style.br)],
              [sg.Text(size=(20,1), k='ERRORMSG')]]
    window = sg.Window('Login', layout, finalize=True, location=(-10, 0), resizable=True, element_justification='c',margins=(0,250))
    window.maximize()
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    return window

def registerDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Register',**style.title)],
              [sg.Input(k='NAME', enable_events=True)],
              [sg.Input(k='EMAIL', enable_events=True)],
              [sg.Input(k='PASSWORD', enable_events=True)],
              [sg.Input(k='REPEATEDPASSWORD', enable_events=True)],
              [sg.Input(k='PHONE', enable_events=True)],
              [sg.Input(k='ADDRESS', enable_events=True)],
              [sg.Button('Login',**style.bl), sg.Button('Register',**style.br)],
              [sg.Text(size=(20,1),  k='ERRORMSG')]]
    window = sg.Window('Register', layout, finalize=True, location=(-10, 0), resizable=True, element_justification='c',margins=(0,250))
    window.maximize()
    utilities.setPlaceholder(window["NAME"], placeholderText="your name")
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    utilities.setPlaceholder(window["REPEATEDPASSWORD"], placeholderText="repeat password")
    utilities.setPlaceholder(window["PHONE"], placeholderText="phone number")
    utilities.setPlaceholder(window["ADDRESS"], placeholderText="address")
    return window