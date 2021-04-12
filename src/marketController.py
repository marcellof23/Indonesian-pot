import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +
                             "@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
db = client.pot
products = db.products


def searchProductController(query: str):
    query = query.lower()
    res = []
    for product in products.find({"title": {"$regex": "\w*" + str(query) + "\w*"}}):
        res.append(product)
    print(res)
    return res
