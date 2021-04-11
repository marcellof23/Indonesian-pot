import PySimpleGUI as sg
from screeninfo import get_monitors

monitor = get_monitors()[0]
windowWidth , windowHeight = monitor.width, monitor.height 

def marketDisplay():
    layout = [[sg.Text('Market')],
               [sg.Button('< Prev'), sg.Button('Next >')]]

    return sg.Window('Window 2', layout, finalize=True, size= (windowWidth,windowHeight))