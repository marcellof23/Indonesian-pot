import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv
import copy
from bson import ObjectId
import cartController

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")

db = client.pot
carts = db.cart
product = db.products
order = db.orders
payment = db.payments

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
        if (j['count'] <= j['stok']):
            sum += (j['count']*j['harga'])
    return sum

def addPaymentFromOrder(user : dict):
    objectIdList = []
    x = order.find({"idPembeli":user["_id"],"status":"belum dibayar"})
    for i in x:
        objectIdList.append(i['_id'])
    payment.insert_one({"listOrderObjectId":objectIdList,"nominal":getTotalPrice(user)+10000,"status":"belum dibayar"})
    cartController.clearProductFromCart(user)



def updatePayment(user : dict):
    
    x = order.find({"idPembeli":user["_id"],"status":"belum dibayar"})
    for i in x:
        order.find_one_and_update({"_id":i["_id"]},{'$set' : {'status' : "dalam pengiriman"}})
        payment.find_one_and_update({"listOrderObjectId":i["_id"]}, {'$set' : {'status' : "sudah dibayar"}})