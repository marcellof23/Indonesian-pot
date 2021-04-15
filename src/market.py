import PySimpleGUI as sg
import utilities


def makeTanamanCard(data):
    return [[sg.Button(button_text=data['title'], key=f"{data['title']},{data['_id']}", button_color="#ccffff")], [sg.Multiline(data['deskripsi'], background_color="#ccffff", size=(18, 6), no_scrollbar=True, pad=(25, 0))], [sg.Text(data['harga'], background_color="#ccffff")]]


def makeTanamanDetail(data):
    key = data["_id"]
    return [[sg.Text(data['title'], background_color="#ccffff")],
            [sg.Text(data['harga'], background_color="#ccffff")],
            [sg.Text(data['deskripsi'], background_color="#ccffff"), ],
            [sg.Text(text="Kategori : " + data['kategori'],
                     background_color="#ccffff")],
            [sg.Text(text="Stok : " + str(data['stok']),
                     background_color="#ccffff")],
            [sg.Text(text="Kuantitas : " + str(1), size=(20, 1),
                     background_color="#ccffff", k="KUANTITAS")],
            [sg.Button(button_text='Kurang', key="ADD"),
             sg.Button(button_text='Tambah', key="REDUCE")],
            [sg.Button(button_text='Add to Cart', key=f"ADDTOCART,{key}")]]


def marketDisplay(windowWidth: int, windowHeight: int, data, isDetail, detailData):
    layout1 = [[sg.Image(key="-IMAGE-", size=(20, 20)),
                sg.Input(k='QUERY', do_not_clear=True), sg.Button('Search'), sg.ButtonMenu('Kategori', ['Unused', ['Tanaman Hias', 'Tanaman Obat', 'Tanaman Langka']], k="KATEGORI"), sg.Button('Store'), sg.Button('Cart'), sg.Button('Profile')]]

    layout2 = [[sg.Text('List Tanaman', background_color='white')], [
        sg.Text(size=(50, 1), k='ERRORMSG', pad=(0, 0), background_color='white'))]]
    container_layout2=[[]]
    list_layout2=[]
    i=1
    itr=i
    if(not(isDetail)):
        for row in data:
            if(itr % 3 == 0):
                list_layout2 += sg.Column(makeTanamanCard(row), key = f'-COL{i}-',
                                          background_color = '#ffccff', size = (220, 200), pad = (180, 20), element_justification = 'c'),
                container_layout2 += [list_layout2]
                list_layout2=[]
                itr=0
            else:
                list_layout2 += sg.Column(makeTanamanCard(row), key = f'-COL{i}-',
                                          background_color = '#ffccff', size = (220, 200), pad = (180, 0), element_justification = 'c'),
            itr += 1
            i += 1

    else:
        list_layout2 += sg.Column(makeTanamanDetail(detailData), key = '-COL1-',
                                  background_color='#ffccff'),

    container_layout2 += [list_layout2]
    layout2 += container_layout2
    layout = [[sg.Column(layout1, key='HEADER', background_color='#ccffff',
                         size=(windowWidth, 200), pad=(0, 0))],
              [sg.Column(layout2, key='BODY', background_color='white',
                         size=(windowWidth, windowHeight-200), pad=(0, 0))]]
    window = sg.Window('Market', layout, margins=(0, 0), finalize=True, size=(
        windowWidth, windowHeight), location=(-10, 0))
    utilities.insertImage(500, 500, window)
    return window
