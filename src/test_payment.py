import pymongo
import sys
import os
from bson import ObjectId
from cartController import addProductToCart, reduceCartProduct
from paymentController import getTotalPrice, addPaymentFromOrder
from authController import loginAuthController
from marketController import searchProductByTitleController, searchProductByCategoryController


class TestPayment:
    def test_paymentOne(self):
        status = "FALSE"
        user = loginAuthController("test", "test")
        product = searchProductByTitleController("kaktus")
        addProductToCart(user['_id'], product[0]['_id'], 2)
        totalPrice = getTotalPrice(user)
        if(totalPrice == 100000) :
            status = "TRUE"
        reduceCartProduct(user['_id'], product[0]['_id'])
        reduceCartProduct(user['_id'], product[0]['_id'])
        assert status == "TRUE"
        
