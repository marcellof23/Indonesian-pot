import PySimpleGUI as sg
import style
import cartController
import utilities


def cartDisplay(windowWidth : int,windowHeight : int,user:dict):
    layout1= [[sg.Image(key="-IMAGE-", size=(20, 20)),
                sg.Button('Store'), sg.Button('Profile')]]
    cartData = cartController.getCartProduct(user)
    if(len(cartData)>0):
        for data in cartData:
            key = data["_id"]
            price = str(data['count']*data['harga'])
            layout1 += [
                [sg.Text('Profile\t\t',**style.normal),sg.Column([[sg.Text(text=data['title'],key=data['title'],size=(20,1),**style.normal)],[sg.Text(text=data['harga'],key=f"HARGA {key}",size=(20,1),**style.normal)]]),sg.Text(text='\t' +str(data['count']) + '\t',key=f'COUNT {key}',size=(10,1),**style.normal),sg.Text(text=price + '\t', key=f'HARGATOTAL {key}',size=(20,1),**style.normal),sg.Button(button_text='-',key=f"REDUCE {key}",**style.bd),sg.Button(button_text='+',key=f"ADD {key}",**style.bd)],
                [sg.Text('\n\n')]
                ]
    else:
        layout1 += [[sg.Text('Cart kosong, belanja yuk', **style.normal)]]
    layout1 += [[sg.Button('Checkout',**style.br)]]
    layout = [[sg.Column(layout1, key='-C-', vertical_alignment='top', justification='center', scrollable=True, vertical_scroll_only=True, k='-C-',pad=((550,0),(0,0)))]]
    window = sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0),resizable=True,element_justification='c')
    window['-C-'].expand(True, True, True)
    utilities.insertImage(500, 500, window)
    return window