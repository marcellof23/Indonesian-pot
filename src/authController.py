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
    email = email.lower()
    print(email, password)
    x = users.find_one({"email": email})
    print(x)
    return x

def registerAuthController(name: str,email: str, password: str, repeatedpassword: str, phonenumber: str, address: str):
    email = email.lower()
    if(sha256(password.encode()).hexdigest() == sha256(repeatedpassword.encode()).hexdigest()):
        user = users.find_one({"email": email})
        if(user):
            return "EMAILREGISTERED"
        else:
            x = users.insert_one({"nama": name,"email": email, "password": password, "telp": phonenumber, "alamat": address})
            return x
    else:
        return "PASSNOTMATCH"

password = "tampandanberani"
print(sha256(password.encode()).hexdigest())