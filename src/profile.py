import PySimpleGUI as sg
import style
import utilities

def profileDisplay(windowWidth : int,windowHeight : int,user : dict):
    layout = [[sg.Image(key="-IMAGE-", size=(20, 20)), sg.Button('Store'), sg.Button('Cart'), sg.Button('Logout')],
              [sg.Text('Nama \t:  ',**style.title),sg.Text(user['nama'],**style.title)],
              [sg.Text('Email \t:  ',**style.title),sg.Text(user['email'],**style.title)]]
    window = sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))
    utilities.insertImage(500, 500, window)
    return window