import PySimpleGUI as sg


def makeLayout(data):
    return [[sg.Text(data['title'], background_color="#ccffff")], [sg.Text(data['deskripsi'], background_color="#ccffff")], [sg.Text(data['harga'], background_color="#ccffff")]]


def marketDisplay(windowWidth: int, windowHeight: int, data):
    layout1 = [[sg.Text('Indonesian - Pot', background_color="#ccffff"),
                sg.Input(k='QUERY', do_not_clear=True), sg.Button('Search'), sg.Button('Store'), sg.Button('Forum'), sg.Button('Tips & Tricks'), sg.Button('Cart'), sg.Button('Logout')]]

    layout2 = [[sg.Text('List Tanaman', background_color='white')]]

    for row in data:
        i = 1
        layout2 += [[sg.Column(makeLayout(row), key=f'-COL{i}-',
                               background_color='#ffccff')]]
        i += 1

    layout = [[sg.Column(layout1, key='HEADER', background_color='#ccffff',
                         size=(windowWidth, 200))], [sg.Column(layout2, key='BODY', background_color='white', size=(windowWidth, windowHeight-300))],
              [sg.Text(size=(20, 1), k='ERRORMSG')]]

    return sg.Window('Market', layout, finalize=True, size=(windowWidth, windowHeight), location=(-10, 0))
