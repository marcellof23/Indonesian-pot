import PySimpleGUI as sg
import style
import paymentController
import utilities


def paymentDisplay(windowWidth : int,windowHeight : int,totalPrice : int):
    layout = [[sg.Text('\n',**style.title)],
                [sg.Image(key="-IMAGE-", size=(20, 20))],
                [sg.Text('\n\nTotal harga : ' + str(totalPrice),**style.totalPrice)],
                [sg.Text('Biaya Pengiriman : ' + "10000",**style.totalPrice)],
                [sg.Button('Pay',**style.br)]]
    window = sg.Window('Payment', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0),resizable=True,element_justification='c')
    utilities.insertImage(500,500,window)
    return window