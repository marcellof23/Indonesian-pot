import PySimpleGUI as sg

def marketDisplay(windowWidth : int, windowHeight : int):
    layout = [[sg.Text('Market')],
               [sg.Button('< Prev'), sg.Button('Next >')]]

    return sg.Window('Window 2', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))