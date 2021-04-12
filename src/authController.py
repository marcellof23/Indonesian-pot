import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
print("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +"@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
db = client.pot
users = db.users

def loginAuthController(email: str,password: str):
    print(email, password)
    x = users.find_one({"email": email})
    print(x)
    return x

def registerAuthController(name: str):
    x = users.find_one({"nama": name})
    print(x)

password = "Alexandria327"
print(sha256(password.encode()).hexdigest())