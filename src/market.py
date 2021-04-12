import PySimpleGUI as sg


def makeTanamanCard(data):
    return [[sg.Button(button_text=data['title'], button_color="#ccffff")], [sg.Text(data['deskripsi'], background_color="#ccffff")], [sg.Text(data['harga'], background_color="#ccffff")]]


def makeTanamanDetail(data):
    return [[sg.Text(data['title'], background_color="#ccffff")],
            [sg.Text(data['harga'], background_color="#ccffff")],
            [sg.Text(data['deskripsi'], background_color="#ccffff")],
            [sg.Text(text="Kategori : " + data['kategori'],
                     background_color="#ccffff")],
            [sg.Text(text="Stok : " + str(data['stok']),
                     background_color="#ccffff")],
            [sg.Text(text="Kuantitas : " + str(1), size=(20, 1),
                     background_color="#ccffff", k="KUANTITAS")],
            [sg.Button('Kurang'), sg.Button('Tambah')],
            [sg.Button('Add to Cart')]]


def marketDisplay(windowWidth: int, windowHeight: int, data, isDetail, detailData):
    layout1 = [[sg.Text('Indonesian - Pot', background_color="#ccffff"),
                sg.Input(k='QUERY', do_not_clear=True), sg.Button('Search'), sg.Button('Store'), sg.Button('Forum'), sg.Button('Tips & Tricks'), sg.Button('Cart'), sg.Button('Logout')]]

    layout2 = [[sg.Text('List Tanaman', background_color='white')]]

    if(not(isDetail)):
        i = 1
        for row in data:
            layout2 += [[sg.Column(makeTanamanCard(row), key=f'-COL{i}-',
                                   background_color='#ffccff')]]
            i += 1
    else:
        layout2 += [[sg.Column(makeTanamanDetail(detailData), key='-COL1-',
                               background_color='#ffccff')]]

    layout = [[sg.Column(layout1, key='HEADER', background_color='#ccffff',
                         size=(windowWidth, 200))],
              [sg.Column(layout2, key='BODY', background_color='white',
                         size=(windowWidth, windowHeight-300))],
              [sg.Text(size=(20, 1), k='ERRORMSG')]]

    return sg.Window('Market', layout, finalize=True, size=(windowWidth, windowHeight), location=(-10, 0))
