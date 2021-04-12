import PySimpleGUI as sg

def profileDisplay(windowWidth : int,windowHeight : int):
    layout = [[sg.Text('Profile')],
               [sg.Button('Exit')]]
    return sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))