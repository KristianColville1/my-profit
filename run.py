import os
from pymongo import MongoClient

try:
    
    en_read = os.environ.get('MONGOPASSWORD')
    password = en_read['password']
except Exception:
    print('no luck')


cluster = MongoClient(f"mongodb+srv://rapid_silver_educate:{password}@rapidsilver.h5hbo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['RapidSilver']
collection = db['users']

user_name = input('Enter your username: ')
password = input('Enter your password: ')



post = {"_id":"testing-password", user_name:password, "data":"company"}
collection.insert_one(post)
