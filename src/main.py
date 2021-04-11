import PySimpleGUI as sg
from screeninfo import get_monitors

import auth
import market
import profile

sg.theme('LightGrey3')

windowWidth, windowHeight = None, None

monitors = get_monitors()
if(monitors):
    monitor = monitors[0]
    windowWidth , windowHeight = monitor.width, monitor.height
else:
    windowWidth , windowHeight = 1920, 1080

loginScreen, registerScreen, marketScreen, profileScreen = auth.loginDisplay(windowWidth, windowHeight), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if window == loginScreen:
        if event == 'Login':
            loginScreen.close()
            marketScreen = market.marketDisplay(windowWidth, windowHeight)
        if event == 'Register':
            loginScreen.close()
            registerScreen = auth.registerDisplay(windowWidth, windowHeight)

    if window == registerScreen:
        if event == 'Register':
            registerScreen.close()
            marketScreen = market.marketDisplay(windowWidth, windowHeight)
        elif event == 'Login':
            registerScreen.close()
            loginScreen = auth.loginDisplay(windowWidth, windowHeight)

    if window == marketScreen:
        if event == 'Next >':
            marketScreen.close()
            profileScreen = profile.profileDisplay(windowWidth, windowHeight)
        elif event == '< Prev':
            marketScreen.close()
            loginScreen = auth.loginDisplay(windowWidth, windowHeight)

    if window == profileScreen:
        profileScreen.close()
        marketScreen = market.marketDisplay(windowWidth, windowHeight)

window.close()