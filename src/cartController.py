import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")

db = client.pot
cart = db.cart
product = db.products

def showCartProduct(user : dict):
    z=[]
    print(user)
    x = cart.find_one({"userId":user["_id"]})
    a = x['item']
    for i in a:
        y = (product.find_one({"_id": i["itemid"]}))
        y['value'] = i["value"]
        z.append(y)
    return(z)

