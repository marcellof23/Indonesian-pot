import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +
                             "@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
db = client.pot
products = db.products


def searchProductByTitleController(query: str):
    query = query.lower()
    res = []
    for product in products.find({"title": {"$regex": "\w*" + str(query) + "\w*"}, "aktif": True}, {"userID": 0}):
        res.append(product)
    return res


def searchProductByCategoryController(query: str):
    res = []
    for product in products.find({"kategori": {"$regex": "\w*" + str(query) + "\w*"}, "aktif": True}, {"userID": 0}):
        res.append(product)
    return res
