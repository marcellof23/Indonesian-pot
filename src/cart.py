import PySimpleGUI as sg
import style

def profileDisplay(windowWidth : int,windowHeight : int):
    layout1 = [
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')],
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text('Nama',**style.normal)],[sg.Text('Harga',**style.normal)]]),sg.Text('\tJumlah\t',**style.normal),sg.Text('Total Harga\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n')]
              ]
    # layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0),background_color='black')],  # the thing that expands from top
    #           [sg.Text('', pad=(0,0),key='-EXPAND2-',background_color='red'),              # the thing that expands from left
    #            sg.Column(layout1, vertical_alignment='top', justification='center', scrollable=True, vertical_scroll_only=True, k='-C-',background_color='yellow')]]

    layout = [[sg.Column(layout1, key='-C-', vertical_alignment='top', justification='center', scrollable=True, vertical_scroll_only=True, k='-C-',pad=((550,0),(0,0)))]]
    window = sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0),icon=r'resource/Icon.ico',resizable=True,element_justification='c')
    window['-C-'].expand(True, True, True)
    # window['-EXPAND-'].expand(True, True, True)
    # window['-EXPAND2-'].expand(True, True, True)
    # layout = [[sg.Column(layout1 ,size=(960,windowHeight),scrollable=True, vertical_scroll_only=True,background_color='yellow',element_justification='c')]]
    # layout0 = [[sg.Column(layout)]]
    return window