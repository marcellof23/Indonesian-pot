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

def getTotalPrice(user : dict):
    z=[]
    sum =0
    x = carts.find_one({"userId":user["_id"]})
    if(x):
        a = x['item']
        for i in a:
            y = (product.find_one({"_id": i["itemId"]}))
            y['count'] = i["count"]
            z.append(y)
    for j in z:
        sum += (j['count']*j['harga'])
    return sum