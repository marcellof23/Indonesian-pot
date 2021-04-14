import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")

db = client.pot
carts = db.cart
product = db.products

def getCartProduct(user : dict):
    z=[]
    print(user)
    x = carts.find_one({"userId":user["_id"]})
    if(x):
        a = x['item']
        for i in a:
            y = (product.find_one({"_id": i["itemid"]}))
            y['value'] = i["value"]
            z.append(y)
    return(z)

def reduceCartProduct(userId, productId):
    status = "FAILED"
    cart = carts.find_one({"userId" : userId})
    print("Product Id: " + productId)
    print(cart)
    items = cart["item"]
    for item in items:
        if(str(item["itemid"])==str(productId)):
            print("AAAAAAAAAAAAAAAA")
            if(item['value']>1):
                item['value'] -= 1
                status = "UPDATE"
            else:
                items.remove(item)
                status = "REFRESH"
    print(cart)
    carts.find_one_and_update({"userId":userId}, {'$set': {'item' : items}})
    return status

def addCartProduct(userId, productId):
    status = "FAILED"
    cart = carts.find_one({"userId" : userId})
    items = cart["item"]
    for item in items:
        if(str(item["itemid"])==str(productId)):
            item['value']+=1
            status = "UPDATE"
    carts.find_one_and_update({"userId":userId}, {"$set": {'item': items}})
    return status
