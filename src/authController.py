import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
print("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
db = client.pot
users = db.users

def loginAuthController(name: str,password: str):
    print(name, password)
    x = users.find_one({"nama": name})
    print(x)

def registerAuthController(name: str):
    x = users.find_one({"nama": name})
    print(x)