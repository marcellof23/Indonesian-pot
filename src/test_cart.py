import pytest
import sys, os
from cartController import *
from authController import loginAuthController
from bson import ObjectId

class TestCart:
    
    def test_cart_one(self):
        user = loginAuthController("abc", "bambang")
        status = addCartProduct(user["_id"], "60731e2b67fb9a7089e20f4b")
        assert status == "UPDATE"
    def test_cart_two(self):
        user = loginAuthController("abc", "bambang")
        status = reduceCartProduct(user["_id"], "60731e2b67fb9a7089e20f4b")
        assert status == "UPDATE"
    def test_cart_three(self):
        user = loginAuthController("abc", "bambang")
        status = addProductToCart(user["_id"], "60731e2b67fb9a7089e20f4b", 2)
        assert status == "UPDATE"
    def test_cart_four(self):
        user = loginAuthController("abc", "bambang")
        stockEnough = addOrderFromCart(user)
        assert stockEnough == True
    def test_cart_five(self):
        user = loginAuthController("adm", "123")
        listProduct = []
        clearProductFromCart(user)
        listProduct = getCartProduct(user)
        checkEmpty = checkIsCartEmpty(listProduct)
        assert checkEmpty == True
    def test_cart_six(self):
        user = loginAuthController("abc", "bambang")
        status = "FALSE"
        listProduct = []
        status2 = addProductToCart(user["_id"], "60755c29c8f8a9c0caa47f76", 2)
        status3 = addProductToCart(user["_id"], "60755c55c8f8a9c0caa47f77", 2)
        listProduct = getCartProduct(user)
        for x in range(len(listProduct)):
            for y in range(len(listProduct)):
                if listProduct[x]['_id'] != listProduct[y]['_id'] and listProduct[x]['title'] == listProduct[y]['title'] and x != y:
                    status = "TRUE"
                    break
        assert status == "TRUE"