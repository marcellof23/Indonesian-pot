import PySimpleGUI as sg
from screeninfo import get_monitors

import auth
import market
import profile

monitor = get_monitors()[0]
windowWidth , windowHeight = monitor.width, monitor.height 

loginScreen, marketScreen, profileScreen = auth.loginDisplay(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == loginScreen and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == loginScreen:
        if event == 'Next >':
            loginScreen.hide()
            marketScreen = market.marketDisplay()
        loginScreen['-OUTPUT-'].update(values['-IN-'])

    if window == marketScreen:
        if event == 'Next >':
            marketScreen.hide()
            profileScreen = profile.profileDisplay()
        elif event in (sg.WIN_CLOSED, '< Prev'):
            marketScreen.close()
            loginScreen.un_hide()

    if window == profileScreen:
        profileScreen.close()
        marketScreen.un_hide()

window.close()