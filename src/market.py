import PySimpleGUI as sg


def makeTanamanLayout():
    return [[sg.Button(button_text='Tes', s=(12, 7), button_color='#ffccff'), ], [sg.Text('tes2', background_color="#ccffff", size=(12, 7))]]


def marketDisplay(windowWidth: int, windowHeight: int):
    layout1 = [[sg.Text('Indonesian - Pot', background_color="#ccffff"),
                sg.Input(k='QUERY', enable_events=True), sg.Button('Search'), sg.Button('Store'), sg.Button('Forum'), sg.Button('Tips & Tricks'), sg.Button('Cart'), sg.Button('< Prev'), sg.Button('Next >')]]

    layout2 = [
        [sg.Text('List Tanaman', background_color='white', justification='center')]]

    container_layout2 = [[]]
    list_layout2 = []
    for i in range(5):
        list_layout2 += sg.Column(makeTanamanLayout(), key=str(i),
                                  background_color='#ffccff', pad=(125, 0)),

    container_layout2 = [list_layout2]
    layout2 += container_layout2

    layout = [[sg.Column(layout1, key='-COL1-', background_color='#ccffff',
                         size=(windowWidth, 200))], [sg.Column(layout2, key='-COL2-', background_color='white', size=(windowWidth, windowHeight-300), justification='center')]]

    return sg.Window('Market', layout, margins=(0, 0), finalize=True, size=(windowWidth, windowHeight), location=(-10, 0), element_justification='c', resizable=True)
    # layout = [
    #           [sg.Listbox(values=[], enable_events=True,
    #                       size=(150, 20), k='SEARCHRESULT')],
    #           [sg.Text(size=(20, 1), k='ERRORMSG')],
