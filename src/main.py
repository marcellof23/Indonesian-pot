import PySimpleGUI as sg
from screeninfo import get_monitors

# Boundary Functions
import auth
import market
import profile
import utilities
import cart

# Controller Functions
import authController
import marketController
import cartController

sg.theme('LightGrey3')

windowWidth, windowHeight = None, None

if(not utilities.is_docker()):
    monitor = get_monitors()[0]
    windowWidth, windowHeight = monitor.width, monitor.height
else:
    windowWidth, windowHeight = 1920, 1080

loginScreen, registerScreen, marketScreen, profileScreen, cartScreen = auth.loginDisplay(
    windowWidth, windowHeight), None, None, None, None

cardKey = []
searchResult = []
kuantitas = 1
stok = 0
user = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    if window == loginScreen:
        if event == 'Login':

            response = authController.loginAuthController(
                values['EMAIL'], values['PASSWORD'])
            if(response):
                user = response
                loginScreen.close()
                marketScreen = market.marketDisplay(
                    windowWidth, windowHeight, [], False, {})
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
                        windowWidth, windowHeight, [], False, {})
            else:
                window['ERRORMSG'].update("Fields must not be empty")
        elif event == 'Login':
            registerScreen.close()
            loginScreen = auth.loginDisplay(windowWidth, windowHeight)

    if window == marketScreen:
        event = event.split(",")
        if(len(event) == 1):
            event.append(None)

        if event[0] == 'Search':
            cardKey.clear()
            searchResult.clear()
            response = marketController.searchProductByTitleController(
                values['QUERY'])
            if(response):
                for row in response:
                    cardKey.append(str(row['_id']))
                    searchResult.append(row)
                marketScreen = market.marketDisplay(
                    windowWidth, windowHeight, response, False, {})
                window.close()
            else:
                window['ERRORMSG'].update("Produk tidak ditemukan!")

        elif event[0] == 'ADD':
            if(kuantitas > 0):
                window['KUANTITAS'].update(
                    "Kuantitas : " + str(kuantitas-1))
                kuantitas -= 1

        elif event[0] == 'REDUCE':
            if(kuantitas < stok):
                window['KUANTITAS'].update(
                    "Kuantitas : " + str(kuantitas+1))
                kuantitas += 1

        elif event[0] == 'ADDTOCART':
            print(event[1])
            print(kuantitas)
            cartController.addProductToCart(user["_id"], event[1], kuantitas)

        elif event[0] == 'KATEGORI':
            cardKey.clear()
            searchResult.clear()
            response = marketController.searchProductByCategoryController(
                values['KATEGORI'])
            if(response):
                for row in response:
                    cardKey.append(str(row['_id']))
                    searchResult.append(row)
                marketScreen = market.marketDisplay(
                    windowWidth, windowHeight, response, False, {})
                window.close()
            else:
                window['ERRORMSG'].update("Produk tidak ditemukan!")

        elif event[1] in cardKey:
            kuantitas = 1
            detail = {}
            for row in searchResult:
                if(row['title'] == event[0]):
                    detail = row
                    stok = row['stok']

            marketScreen.close()
            marketScreen = market.marketDisplay(
                windowWidth, windowHeight, [], True, detail)

        elif event[0] == 'Profile':
            marketScreen.close()
            profileScreen = profile.profileDisplay(
                windowWidth, windowHeight, user)

        elif event[0] == 'Cart':
            cartScreen = cart.cartDisplay(windowWidth, windowHeight, user)
            marketScreen.close()

    if window == profileScreen:
        if event == 'Logout':
            profileScreen.close()
            loginScreen = auth.loginDisplay(windowWidth, windowHeight)
        elif event == 'Store':
            profileScreen.close()
            marketScreen = market.marketDisplay(
                windowWidth, windowHeight, [], False, {})
        elif event == 'Cart':
            profileScreen.close()
            cartScreen = cart.cartDisplay(windowWidth, windowHeight, user)
    if window == cartScreen:
        event = event.split()
        if event[0] == 'Profile':
            cartScreen.close()
            profileScreen = profile.profileDisplay(
                windowWidth, windowHeight, user)
        elif event[0] == 'Store':
            cartScreen.close()
            marketScreen = market.marketDisplay(
                windowWidth, windowHeight, [], False, {})
        elif event[0] == 'REDUCE':
            status = cartController.reduceCartProduct(user["_id"], event[1])
            if(int(window[f'COUNT {event[1]}'].DisplayText) > 1):
                window[f'COUNT {event[1]}'].update(
                    str(int(window[f'COUNT {event[1]}'].DisplayText) - 1))
                window[f'HARGATOTAL {event[1]}'].update(str(int(
                    window[f'COUNT {event[1]}'].DisplayText) * int(window[f'HARGA {event[1]}'].DisplayText)))
            else:
                cartScreen.close()
                cartScreen = cart.cartDisplay(windowWidth, windowHeight, user)
        elif event[0] == 'ADD':
            status = cartController.addCartProduct(user["_id"], event[1])
            window[f'COUNT {event[1]}'].update(
                str(int(window[f'COUNT {event[1]}'].DisplayText) + 1))
            window[f'HARGATOTAL {event[1]}'].update(str(int(
                window[f'COUNT {event[1]}'].DisplayText) * int(window[f'HARGA {event[1]}'].DisplayText)))
window.close()
