import style
import PySimpleGUI as sg
import utilities

password = {''}

def loginDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Image(key="-IMAGE-",size=(20,20))],
              [sg.Text('\nLogin\n',**style.title)],
              [sg.Text('Email\t :',**style.normal),sg.Input(k='EMAIL', enable_events=True)],
              [sg.Text('Password\t :',**style.normal),sg.Input(k='PASSWORD', enable_events=True,password_char='*')],
              [sg.Text('',**style.title)],
              [sg.Button('Login',**style.bl), sg.Button('Register',**style.br)],
              [sg.Text(size=(20,1), k='ERRORMSG')]]
    window = sg.Window('Login', layout, finalize=True, location=(-10, 0), resizable=True, element_justification='c',margins=(0,250))
    window.maximize()
    utilities.insertImage(500,500,window)
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    return window

def registerDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Image(key="-IMAGE-",size=(20,20))],
              [sg.Text('\nRegister\n',**style.title)],
              [sg.Text('Name\t\t :',**style.normal),sg.Input(k='NAME', enable_events=True)],
              [sg.Text('Email\t\t :',**style.normal),sg.Input(k='EMAIL', enable_events=True)],
              [sg.Text('Password\t\t :',**style.normal),sg.Input(k='PASSWORD', enable_events=True,password_char='*')],
              [sg.Text('Repeat Password\t :',**style.normal),sg.Input(k='REPEATEDPASSWORD', enable_events=True,password_char='*')],
              [sg.Text('Phone\t\t :',**style.normal),sg.Input(k='PHONE', enable_events=True)],
              [sg.Text('Address\t\t :',**style.normal),sg.Input(k='ADDRESS', enable_events=True)],
              [sg.Text('',**style.title)],
              [sg.Button('Login',**style.bl), sg.Button('Register',**style.br)],
              [sg.Text(size=(20,1),  k='ERRORMSG')]]
    window = sg.Window('Register', layout, finalize=True, location=(-10, 0), resizable=True, element_justification='c',margins=(0,250))
    window.maximize()
    utilities.insertImage(500,500,window)
    utilities.setPlaceholder(window["NAME"], placeholderText="your name")
    utilities.setPlaceholder(window["EMAIL"], placeholderText="e-mail address")
    utilities.setPlaceholder(window["PASSWORD"], placeholderText="password")
    utilities.setPlaceholder(window["REPEATEDPASSWORD"], placeholderText="repeat password")
    utilities.setPlaceholder(window["PHONE"], placeholderText="phone number")
    utilities.setPlaceholder(window["ADDRESS"], placeholderText="address")
    return window