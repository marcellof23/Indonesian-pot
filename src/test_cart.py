import pytest
import sys, os
from cartController import *
from authController import loginAuthController
from bson import ObjectId

class TestCart:
    
    def test_cart_one(self):
        user = loginAuthController("abc", "bambang")
        cart = getCartProduct(user)
        assert cart[0]['title'] == "eceng gondok"
    def test_cart_two(self):
        user = loginAuthController("abc", "bambang")
        status = addCartProduct(user["_id"], "60731e2b67fb9a7089e20f4b")
        assert status == "UPDATE"
    def test_cart_three(self):
        user = loginAuthController("abc", "bambang")
        status = reduceCartProduct(user["_id"], "60731e2b67fb9a7089e20f4b")
        assert status == "UPDATE"
    def test_cart_four(self):
        user = loginAuthController("abc", "bambang")
        status = addProductToCart(user["_id"], "60731e2b67fb9a7089e20f4b", 2)
        assert status == "UPDATE"
    def test_cart_five(self):
        user = loginAuthController("abc", "bambang")
        stockEnough = addOrderFromCart(user)
        assert stockEnough == False
    def test_cart_six(self):
        user = loginAuthController("adm", "123")
        listProduct = []
        clearProductFromCart(user)
        listProduct = getCartProduct(user)
        checkEmpty = checkIsCartEmpty(listProduct)
        assert checkEmpty == True