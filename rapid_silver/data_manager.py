"""
Data manager hold the DataManager Class for Rapid Silver.
Manages user data for a given user profile.
"""
import os
import time
from pymongo import MongoClient
from rich.table import Table
from rich.console import Console
from console import clear_console
from rapid_silver.text_art import TextArt
from rapid_silver.user import User

# instances created
color = TextArt()


class DataManager():
    """
    Manages user data and accesses the resources for the user when activated.
    Stores the users data entered. Updates the users data. It can only be used
    with the PasswordManagers credentials for the logged in user.
    """

    mongo_link = os.environ.get('MONGOLINK')
    _cluster = MongoClient(f'{mongo_link}')
    _database = _cluster['RapidSilver']
    _user_details_collection = _database['users_details']

    def __init__(self, user_id):
        self.username = user_id
        self.results = self.check_user_details()
        if self.results is None:
            self.user = User()
            self.add_details_to_database(self.username, self.user.user_details)
        else:
            self.print_welcome_back()


    def check_user_details(self):
        """
        Checks to see if user details already exists and returns the result.
        """
        result = self._user_details_collection.find_one({"_id": self.username})
        time.sleep(1)
        return result

    def add_details_to_database(self, user_id, dict_of_user_details):
        """
        Adds details from user class to a dict to send to the details
        collection in MongoDB.
        """
        details_to_send = {}
        details_to_send["_id"] = str(user_id)

        for key, value in dict_of_user_details.items():
            details_to_send[key] = value

        post = details_to_send
        self._user_details_collection.insert_one(post)

    def print_welcome_back(self):
        """
        Welcomes the user back and prints their details to the screen.
        """
        clear_console()
        print('\n\n\n')
        print('Welcome back ', self.username)

        print('Here are  your profile details')
        table = Table()

        user_profile = self._user_details_collection.find_one(self.username)

        table.add_column('Type', style='cyan')
        table.add_column('Details', style='yellow')

        for key, value in user_profile.items():
            table.add_row(key, value)

        console = Console()
        console.print(table)
