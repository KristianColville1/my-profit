"""Hold the password class for Rapid Silver"""
import os
from pymongo import MongoClient
from getpass import getpass
from cryptography.fernet import Fernet
from console import clear_console


class PasswordManager():
    """
    Handles the password information for the user of
    Rapid Silver.
    """
    character_dict = {
        'a': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'b': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y', 'Z']
    }

    character_keys = ['a', 'b']

    profile_dict = {
        "USERNAME": "",
        "PASSWORD": ""
    }

    def __init__(self, account_type):
        # temporary catch claus for local development and live terminal development
        try:
            self.mongopass = os.environ.get('MONGOPASSWORD')
        except NameError:
            file = open('mongodb.txt', encoding='utf8')
            self._mongopass = file.read()
            file.close()
        if account_type == 'new':
            self._set_username()
            self._set_user_password()
            self._log_in_user()
        elif account_type == 'old':
            self._get_login_details()
            self._log_in_user()

    def _set_username(self):
        
        return None
    def _set_user_password(self):
        return ''
    def _log_in_user(self):
        return ''
    def _get_login_details(self):
        return ''
    # TODO: Create salt, pepper and hashing
    # TODO: Store inside a database
    # TODO: block user password from being stored anywhere in plain text
    # TODO: get all code and structure it properly


cluster = MongoClient(f"mongodb+srv://rapid_silver_educate:{password}@rapidsilver.h5hbo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['RapidSilver']
collection = db['users']

user_name = input('Enter your username: ')
password = input('Enter your password: ')


# leave id blank as it needs unique identifiers on each post and it current does not matter
post = { user_name:password, "data":"company"}
collection.insert_one(post)