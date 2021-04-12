import PySimpleGUI as sg
from screeninfo import get_monitors

# Boundary Functions
import auth
import market
import profile
import utilities

# Controller Functions
import authController
import marketController

sg.theme('LightGrey3')

windowWidth, windowHeight = None, None

if(not utilities.is_docker()):
    monitor = get_monitors()[0]
    windowWidth, windowHeight = monitor.width, monitor.height
else:
    windowWidth, windowHeight = 1920, 1080

loginScreen, registerScreen, marketScreen, profileScreen = auth.loginDisplay(
    windowWidth, windowHeight), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if window == loginScreen:
        if event == 'Login':

            response = authController.loginAuthController(
                values['EMAIL'], values['PASSWORD'])
            if(response):
                loginScreen.close()
                marketScreen = market.marketDisplay(
                    windowWidth, windowHeight, [])
            window['ERRORMSG'].update("Failed")

        if event == 'Register':
            loginScreen.close()
            registerScreen = auth.registerDisplay(
                windowWidth, windowHeight)

    if window == registerScreen:
        if event == 'Register':
            validate = len(values['NAME']) > 0 and len(values['EMAIL']) > 0 and len(values['PASSWORD']) > 0 and len(values['REPEATEDPASSWORD']) > 0 and len(values['PHONE']) > 0 and len(
                values['ADDRESS']) > 0 and values['NAME'] != "your name" and values['EMAIL'] != "e-mail address" and values['PASSWORD'] != "password" and values['REPEATEDPASSWORD'] != "repeat password" and values['PHONE'] != "phone number" and values['ADDRESS'] != "address"
            if(validate):
                response = authController.registerAuthController(
                    values['NAME'], values['EMAIL'], values['PASSWORD'], values['REPEATEDPASSWORD'], values['PHONE'], values['ADDRESS'])
                if(response == "PASSNOTMATCH"):
                    window['ERRORMSG'].update(response)
                elif(response == "EMAILALREADYREGISTERED"):
                    window['ERRORMSG'].update(response)
                else:
                    registerScreen.close()
                    marketScreen = market.marketDisplay(
                        windowWidth, windowHeight)
            else:
                window['ERRORMSG'].update("Fields must not be empty")
        elif event == 'Login':
            registerScreen.close()
            loginScreen = auth.loginDisplay(windowWidth, windowHeight)

    if window == marketScreen:
        if event == 'Search':
            response = marketController.searchProductController(
                values['QUERY'])
            if(response):
                marketScreen.close()
                marketScreen = market.marketDisplay(
                    windowWidth, windowHeight, response)
            else:
                window['ERRORMSG'].update("Produk tidak ditemukan!")

        # elif event == 'Next >':
        #     marketScreen.close()
        #     profileScreen = profile.profileDisplay(windowWidth, windowHeight)
        # elif event == '< Prev':
        #     marketScreen.close()
        #     loginScreen = auth.loginDisplay(windowWidth, windowHeight)

    if window == profileScreen:
        profileScreen.close()
        marketScreen = market.marketDisplay(windowWidth, windowHeight)

window.close()
