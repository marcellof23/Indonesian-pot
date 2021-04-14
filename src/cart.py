import PySimpleGUI as sg
import style
import cartController
import utilities


def cartDisplay(windowWidth : int,windowHeight : int,user:dict):
    layout1= [[sg.Image(key="-IMAGE-", size=(20, 20)),
                sg.Button('Store'), sg.Button('Profile')]]
    cartData = cartController.getCartProduct(user)
    if(len(cartData)>0):
        for i in cartData:
            print(i)
            layout1 += [
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text(i['title'],**style.normal)],[sg.Text(i['harga'],**style.normal)]]),sg.Text('\t' +str(i['value'])+'\t',**style.normal),sg.Text(str(i['value']*i['harga']) + '\t',**style.normal),sg.Button('Hapus',**style.bd)],
                [sg.Text('\n\n')]
                ]
            # layout1 += [
            #           [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text(i['title'],**style.normal)],[sg.Text(i['harga'],**style.normal)]]),sg.Text('\t',i['value'],'\t',**style.normal),sg.Text(i['value']*i['harga'],'t',**style.normal),sg.Button('Hapus',**style.bd)],
            #           [sg.Text('\n')]
            #         ]
    else:
        layout1 += [[sg.Text('Cart kosong, belanja yuk', **style.normal)]]
    layout1 += [[sg.Button('Checkout',**style.br)]]
    layout = [[sg.Column(layout1, key='-C-', vertical_alignment='top', justification='center', scrollable=True, vertical_scroll_only=True, k='-C-',pad=((550,0),(0,0)))]]
    window = sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0),resizable=True,element_justification='c')
    window['-C-'].expand(True, True, True)
    utilities.insertImage(500, 500, window)
    return window