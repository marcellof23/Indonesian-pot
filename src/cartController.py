import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv
import copy
from bson import ObjectId

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")

db = client.pot
carts = db.cart
product = db.products

def getCartProduct(user : dict):
    z=[]
    x = carts.find_one({"userId":user["_id"]})
    if(x):
        a = x['item']
        for i in a:
            y = (product.find_one({"_id": i["itemId"]}))
            y['count'] = i["count"]
            z.append(y)
    return(z)

def reduceCartProduct(userId, productId):
    status = "FAILED"
    cart = carts.find_one({"userId" : userId})
    items = cart["item"]
    for item in items:
        if(str(item["itemId"])==str(productId)):
            if(item['count']>1):
                item['count'] -= 1
                status = "UPDATE"
            else:
                items.remove(item)
                status = "REFRESH"
    carts.find_one_and_update({"userId":userId}, {'$set': {'item' : items}})
    return status

def addCartProduct(userId, productId):
    status = "FAILED"
    cart = carts.find_one({"userId" : userId})
    items = cart["item"]
    for item in items:
        if(str(item["itemId"])==str(productId)):
            item['count']+=1
            status = "UPDATE"
    carts.find_one_and_update({"userId":userId}, {"$set": {'item': items}})
    return status

def addProductToCart(userId, productId, amount : int):
    status = "FAILED"
    cart = carts.find_one({"userId" : userId})
    items = cart["item"]
    if(amount>0):
        for item in items:
            if(str(item["itemId"])==str(productId)):
                item['count'] += amount
                status = "UPDATE"
        if(status=="FAILED"):
            newItem = {}
            newItem["itemId"] = ObjectId(productId)
            newItem["count"] = amount
            items.append(copy.deepcopy(newItem))
        carts.find_one_and_update({"userId":userId}, {"$set": {'item': items}})
    return status
