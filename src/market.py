import PySimpleGUI as sg
import utilities
from authController import db
import style

def makeTanamanCard(data, i, windowWidth, windowHeight):
    imgData = bytes(data["imageData"], 'utf-8')
    return [[sg.Button(image_data=imgData, key=f"{data['title']},{data['_id']}", image_subsample=8)], [sg.Text(data['title'], background_color="white", **style.hargaMarket)], [sg.Multiline(data['deskripsi'], background_color="white", size=(int(round((windowWidth/1920)*18)), int(round((windowHeight/1080)*6))), no_scrollbar=True, pad=(int(round((windowWidth/1920)*25)), 0))], [sg.Text(data['harga'], background_color="white", **style.hargaMarket)]]


def makeTanamanDetail(data):
    imgData = bytes(data["imageData"], 'utf-8')
    key = data["_id"]
    return [[sg.Button(button_text=data['title'], image_data=imgData, image_subsample=8)],
            [sg.Text(data['title'], background_color="white")],
            [sg.Text(data['harga'], background_color="white")],
            [sg.Text(data['deskripsi'], background_color="white"), ],
            [sg.Text(text="Kategori : " + data['kategori'],
                     background_color="white")],
            [sg.Text(text="Stok : " + str(data['stok']),
                     background_color="white")],
            [sg.Text(text="Kuantitas : " + str(1), size=(20, 1),
                     background_color="white", k="KUANTITAS")],
            [sg.Button(button_text='Kurang', key="ADD"),
             sg.Button(button_text='Tambah', key="REDUCE")],
            [sg.Button(button_text='Add to Cart', key=f"ADDTOCART,{key}")]]


def marketDisplay(windowWidth: int, windowHeight: int, data, isDetail, detailData):
    layout1 = [[sg.Image(key="-IMAGE-", size=(20, 20), background_color=None),
                sg.Input(k='QUERY', do_not_clear=True), sg.Button('Search'), sg.ButtonMenu('Kategori', ['Unused', ['Tanaman Hias', 'Tanaman Obat', 'Tanaman Langka']], k="KATEGORI", button_color="#83D0C9"), sg.Button('Store', button_color="#35a79c"), sg.Button('Cart', button_color="#83D0C9"), sg.Button('Profile', button_color="#83D0C9")]]

    layout2 = [[sg.Text('List Tanaman', background_color='white',**style.title)], [
        sg.Text(size=(50, 1), k='ERRORMSG', pad=(0, 0), background_color='white')]]
    container_layout2 = [[]]
    list_layout2 = []
    i = 1
    itr = i
    if(not(isDetail)):
        for row in data:
            if(itr % 3 == 0):
                list_layout2 += sg.Column(makeTanamanCard(row, i, windowWidth, windowHeight), key=f'-COL{i}-',
                                          background_color='#ccffff', size=((windowWidth/1920)*220, (windowHeight/1080)*350), pad=((windowWidth/1920)*180, (windowHeight/1080)*50), element_justification='c'),
                container_layout2 += [list_layout2]
                list_layout2 = []
                itr = 0
            else:
                list_layout2 += sg.Column(makeTanamanCard(row, i, windowWidth, windowHeight), key=f'-COL{i}-',
                                          background_color='#ccffff', size=((windowWidth/1920)*220, (windowHeight/1080)*350), pad=((windowWidth/1920)*180, (windowHeight/1080)*50), element_justification='c'),
            itr += 1
            i += 1

    else:
        list_layout2 += sg.Column(makeTanamanDetail(detailData), key='-COL1-',
                                  background_color='#ccffff'),

    container_layout2 += [list_layout2]
    layout2 += container_layout2
    layout = [[sg.Column(layout1, key='HEADER', background_color='#ccffff',
                         size=(windowWidth, (windowHeight/1080)*200), pad=(0, 0),)],
              [sg.Column(layout2, key='BODY', background_color='white',
                         size=(windowWidth, windowHeight-(windowHeight/1080)*200), pad=(0, 0), scrollable=True)]]
    window = sg.Window('Market', layout, margins=(0, 0), finalize=True, size=(
        windowWidth, windowHeight), location=(-10, 0))
    utilities.insertImage(500, 500, window)
    return window
