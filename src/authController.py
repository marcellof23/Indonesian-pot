import pymongo
from hashlib import sha256
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
client = pymongo.MongoClient("mongodb+srv://IndonesiaPot:" + DATABASE_PASSWORD +
                             "@cluster0.zaqu6.mongodb.net/pot?retryWrites=true&w=majority")
db = client.pot
users = db.users


def loginAuthController(email: str, password: str):
    email = email.lower()
    x = users.find_one(
        {"email": email, "password": sha256(password.encode()).hexdigest()})
    return x


def registerAuthController(name: str, email: str, password: str, repeatedpassword: str, phonenumber: str, address: str):
    email = email.lower()
    if(sha256(password.encode()).hexdigest() == sha256(repeatedpassword.encode()).hexdigest()):
        user = users.find_one({"email": email})
        if(user):
            return "EMAILALREADYREGISTERED"
        else:
            x = users.insert_one({"nama": name, "email": email, "password": sha256(
                password.encode()).hexdigest(), "telp": phonenumber, "alamat": address})
            return {"nama": name, "email": email, "telp": phonenumber, "alamat": address}
    else:
        return "PASSNOTMATCH"
