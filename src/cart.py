import PySimpleGUI as sg
import style



def cartDisplay(windowWidth : int,windowHeight : int):
    layout1= []
    layout1 += [
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')]
              ]
    layout = [[sg.Column(layout1, key='-C-', vertical_alignment='top', justification='center', scrollable=True, vertical_scroll_only=True, k='-C-',pad=((550,0),(0,0)))]]
    window = sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0),resizable=True,element_justification='c')
    window['-C-'].expand(True, True, True)
    return window