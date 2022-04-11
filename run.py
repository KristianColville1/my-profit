import os

from pymongo import MongoClient

try:
    password = os.environ.get('MONGOPASSWORD')
except Exception:
    print('Not accessing password')

cluster = MongoClient(f"mongodb+srv://rapid_silver_educate:{password}@rapidsilver.h5hbo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['RapidSilver']
collection = db['users']

user_name = input('Enter your username: ')
password = input('Enter your password: ')



post = {"_id":"testing-password", user_name:password, "data":"company"}
collection.insert_one(post)
