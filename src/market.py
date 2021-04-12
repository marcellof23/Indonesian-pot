import PySimpleGUI as sg


def makeLayout():
    return [[sg.Text('tes1', background_color="#ccffff")], [sg.Text('tes2', background_color="#ccffff")]]


def marketDisplay(windowWidth: int, windowHeight: int):
    layout1 = [[sg.Text('Indonesian - Pot', background_color="#ccffff"),
                sg.Input(k='QUERY', enable_events=True), sg.Button('Search'),sg.Button('Store'), sg.Button('Forum'), sg.Button('Tips & Tricks'), sg.Button('Cart'), sg.Button('< Prev'), sg.Button('Next >')]]

    layout2 = [[sg.Text('List Tanaman', background_color='white')]]
    layout2 += [[sg.Column(makeLayout(), key='-COL3-',
                           background_color='#ffccff')]]
    layout2 += [[sg.Column(makeLayout(), key='-COL4-',
                           background_color='#ffccff')]]
    layout = [[sg.Column(layout1, key='-COL1-', background_color='#ccffff',
                         size=(windowWidth, 200))], [sg.Column(layout2, key='-COL2-', background_color='white', size=(windowWidth, windowHeight-300))]]
    
    return sg.Window('Market', layout, finalize=True, size=(windowWidth, windowHeight), location=(-10, 0))


    # layout = [
    #           [sg.Listbox(values=[], enable_events=True,
    #                       size=(150, 20), k='SEARCHRESULT')],
    #           [sg.Text(size=(20, 1), k='ERRORMSG')],