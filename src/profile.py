import PySimpleGUI as sg
from screeninfo import get_monitors

monitor = get_monitors()[0]
windowWidth , windowHeight = monitor.width, monitor.height 

def profileDisplay():
    layout = [[sg.Text('Profile')],
               [sg.Button('< Prev'), sg.Button('Exit')]]
    return sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight))