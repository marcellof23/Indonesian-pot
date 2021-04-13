import PySimpleGUI as sg
import style

def profileDisplay(windowWidth : int,windowHeight : int,user : dict):
    layout = [[sg.Text('Indonesian - Pot'), sg.Button('Store'), sg.Button('Forum'), sg.Button('Tips & Tricks'), sg.Button('Cart'), sg.Button('Logout')],
              [sg.Text('Nama \t:  ',**style.title),sg.Text(user['nama'],**style.title)],
              [sg.Text('Email \t:  ',**style.title),sg.Text(user['email'],**style.title)]]
    return sg.Window('Profile', layout, finalize=True, size= (windowWidth,windowHeight), location=(-10, 0))