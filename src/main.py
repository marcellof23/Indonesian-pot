import PySimpleGUI as sg
from screeninfo import get_monitors

# Boundary Functions
import auth
import market
import profile
import utilities

# Controller Functions
import authController

sg.theme('LightGrey3')

windowWidth, windowHeight = None, None

if(not utilities.is_docker()):
    monitor = get_monitors()[0]
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
            response = authController.loginAuthController(values['EMAIL'],values['PASSWORD'])
            if(response):
                loginScreen.close()
                marketScreen = market.marketDisplay(windowWidth, windowHeight)
            window['ERRORMSG'].update("Failed")
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