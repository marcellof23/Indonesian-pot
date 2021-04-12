import PySimpleGUI as sg


def marketDisplay(windowWidth: int, windowHeight: int):
    layout = [[sg.Text('Market')],
              [sg.Input(k='QUERY', enable_events=True)],
              [sg.Button('Search')],
              [sg.Listbox(values=[], enable_events=True,
                          size=(150, 20), k='SEARCHRESULT')],
              [sg.Text(size=(20, 1), k='ERRORMSG')],
              [sg.Button('< Prev'), sg.Button('Next >')]]

    return sg.Window('Market', layout, finalize=True, size=(windowWidth, windowHeight), location=(-10, 0))
