import PySimpleGUI as sg
from screeninfo import get_monitors

import auth
import market
import profile

sg.theme('LightGrey6')

monitor = get_monitors()[0]
windowWidth , windowHeight = monitor.width, monitor.height 

loginScreen, registerScreen, marketScreen, profileScreen = auth.loginDisplay(), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if window == loginScreen:
        if event == 'Login':
            loginScreen.close()
            marketScreen = market.marketDisplay()
        if event == 'Register':
            loginScreen.close()
            registerScreen = auth.registerDisplay()

    if window == registerScreen:
        if event == 'Next >':
            registerScreen.close()
            marketScreen = market.marketDisplay()
        elif event == 'Login':
            registerScreen.close()
            loginScreen = auth.loginDisplay()

    if window == marketScreen:
        if event == 'Next >':
            marketScreen.close()
            profileScreen = profile.profileDisplay()
        elif event == '< Prev':
            marketScreen.close()
            loginScreen = auth.loginDisplay()

    if window == profileScreen:
        profileScreen.close()
        marketScreen = market.marketDisplay()

window.close()