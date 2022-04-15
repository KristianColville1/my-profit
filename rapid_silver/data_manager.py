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
    _to_do_collection = _database['to_do_lists']
    _products_collection = _database['products']
    _employees_collection = _database['inventory']

    def __init__(self, user_id, the_route):
        self.username = user_id
        self.results = self.check_user_details()

        if the_route == 'profile':
            if self.results is None:
                self.user = User()
                self.add_details_to_database(
                    self.username, self.user.user_details)
                self.print_welcome_back()
        elif the_route == 'to_do':
            self.open_to_do_list()
        elif the_route == 'products':
            pass
        elif the_route == 'employee':
            pass
        elif the_route == 'inventory':
            pass

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
            table.add_row(str(key), str(value))

        console = Console()
        console.print(table)

        print(
            color.green_fore(
                '\n\n\t\tHit [ y ] + Enter to change your details'))
        print(
            color.green_fore(
                '\t\tHit [ n ] + Enter to return to options menu'))
        result = input('\nEnter selection here: ')

        if result in ('Y', 'y'):
            self.update_profile(self.username, self.user.user_details)
        elif result in ('N', 'n'):
            # heads back to the selection menu from here
            pass
        else:
            print(
                color.red_fore(
                    'INVALID INPUT. Please select a valid option'))
            time.sleep(2)
            self.print_welcome_back()  # uses recursion until input valid

    def update_profile(self, user_id, dict_of_user_details):
        """
        Takes a profile and updates that document on the Mongo Database.
        """
        user = User()  # creates a new user object
        details_to_send = user.user_details  # gets the details
        details_to_send["_id"] = str(user_id)

        for key, value in dict_of_user_details.items():
            details_to_send[key] = value

        post = details_to_send
        self._user_details_collection.update(user_id, post)  # updates database
        self.print_welcome_back()

    def open_to_do_list(self):
        """
        A user of Rapid Silver can create and update a to do list.
        Checks for existing to do list and if theres none there creates one
        for the user.
        """
        empty_dict = {}
        clear_console()
        to_do_list = self._to_do_collection.find_one({"_id": self.username})
        if to_do_list is None:
            empty_dict["_id"] = self.username
            print(
                color.red_fore(
                    'There are no to do lists matching our records for you'))
            print(
                color.yellow_fore('\n Lets make one now.')
            )
            while True:
                try:
                    key = str(input(
                        color.purple_fore(
                            "\n\nEnter a name for the task here: ")))
                    value = str(input(
                        color.yellow_fore(
                            '\nEnter your task here:')))
                    to_move_on = str(input(
                        color.green_fore(
                            'To create another task hit [ y ] + Enter : ')))

                    if to_move_on not in ('Y', 'y'):
                        break
                    empty_dict[key] = value
                except ValueError:
                    pass
                except TypeError:
                    pass
            self._to_do_collection.insert_one(empty_dict)
        # after a list is either found or made, print it to the terminal
        # calls to get the document again so both routes are
        # accounted for and joined back here
        to_do_list = self._to_do_collection.find_one({"_id": self.username})
        table = Table()
        table.add_column('Name', style='Magenta')
        table.add_column('Task', style='yellow')

        for key, value in to_do_list.items():
            # hides the id and username
            if key == '_id':
                pass
            table.add_row(str(key), str(value))

        console = Console()
        console.print(table)

        print(color.blue_fore(
            "\nWould you like to update your to do list?"
        ))
        print(
            "Hit [ y ] + enter to update your to do list: "
        )

        result = color.green_fore(
            'Enter your choice here, hit enter to skip: '
        )
        color.dot_loading('Updating selections now')
        if result not in ('y', 'Y'):
            pass
        else:
            self.clear_update_to_do_list()

    def clear_update_to_do_list(self):
        """
        Clears or makes amendments to a to do list for a user.
        """
        new_to_do = {"_id": self.username}
        clear_console()
        to_do_list = self._to_do_collection.find_one({"_id": self.username})
        print('\n\n\n\n')
        result = input(color.purple_fore(
            'Do you want to clear or update your to do list?'))
        print(color.yellow_fore(
            'Hit [ y ] + Enter to clear your entire task list and start over '
        ))
        print(color.yellow_fore(
            'Hit [ n ] + Enter to amend individual tasks '
        ))
        if result in ('y', 'Y'):
            self._to_do_collection.delete_one({"_id": self.username})
        if result in ('N', 'n'):
            for key, value in to_do_list.items():
                if key is not "_id":
                    print(f"Update {key} task hit [ y ] + Enter to amend")
                    print("Hit [ n ] + Enter to skip")
                    result = input(color.green_fore('\n\nEnter here: '))
                    if result in ('Y', 'y'):
                        new_key = input('\nEnter the name of the task here: ')
                        new_to_do[new_key] = input(color.yellow_fore(
                            "Enter your task here: "
                        ))
                    if result in ('N', 'n'):
                        new_key[key] = value
        self.open_to_do_list()
