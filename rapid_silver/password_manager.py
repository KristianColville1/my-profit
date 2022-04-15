"""Hold the password class for Rapid Silver"""
import os
import time
import random
from getpass import getpass
from types import new_class
import bcrypt
from pymongo import MongoClient
from console import clear_console
from rapid_silver.text_art import TextArt

# instance created
color = TextArt()
loader = color


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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    special_chars = ['!', '@', '#', '$', '%', '&', '*']



    mongo_link = os.environ.get('MONGOLINK')
    _cluster = MongoClient(f'{mongo_link}')
    _database = _cluster['RapidSilver']
    _collection = _database['users']

    def __init__(self, account_type):
        self.username = None
        self._password = None
        self.user_mongo_dict = {
        "_id": "",
        "password": "",
        }
        # decides which route to take for the account type
        if account_type == 'new':
            self.username = self._set_username()
            self._password = self._set_user_password()
            self._save_user_credentials()
            self._log_in_user()
        elif account_type == 'old':
            self._log_in_user()

    def _set_username(self):
        """
        Checks if the user wishes to either create a username
        or have one assigned to them.
        """
        try:
            clear_console()
            for _ in range(8):
                print('\n')
            print(color.purple_fore(
                'Hit [ e ] + Enter to create a username'))
            print(color.purple_fore(
                'Hit [ d ] + Enter to auto assign a username to yourself'))
            result = str(input(color.green_fore('\nEnter here: ')))

            print(color.cyan_fore('/nChecking username now'))
            if result in ('D', 'd'):
                self.username = self._generate_username()

            elif result in ('e', 'E'):

                clear_console()
                try:

                    advice = color.yellow_fore('Please include (A-Z & a-z)')
                    advice += color.cyan_fore('and at least 1 number')
                    print(advice)
                    username_input = input('Please enter a username: ')

                    if len(username_input) < 8:
                        raise ValueError(
                            'Username must be at least 8 characters'
                            )
                    if len(username_input) > 40:
                        raise ValueError(
                            'Username must be less than 40 characters'
                            )
                    user = username_input
                    input_type = 'username'
                    validation = self._check_characters_valid_in(
                        input_type, user)
                    if validation is False:
                        raise ValueError(
                            'You must include at least one number')
                    name_checker = self.check_database_usernames(
                        username_input)
                    if name_checker is not None:
                        print(color.red_fore(
                            '\n\nUsername is already taken'))
                        print('\n\nPlease try again!')
                        time.sleep(2.5)
                        self._set_username()  # if name taken use recursion
                    self.username = username_input
                except ValueError as error:
                    error = color.red_fore(error)
                    print(error)
                    time.sleep(1.5)
                    self._set_username()
                except TypeError:
                    time.sleep(1.5)
                    self._set_username()

            else:
                print("INVALID Input received.")
                time.sleep(1.5)
                self._set_username()
        except TypeError:
            print('Sorry something went wrong. Let us try that again.')
            time.sleep(3)
            self._set_username()

        return self.username

    def _generate_username(self):
        """
        Generates a username for the user, a combination of letters
        and numbers.
        """
        username = ''
        rand_key = self.character_keys[random.randrange(1)]

        for _ in range(8):
            rand_key = self.character_keys[random.randrange(2)]
            arr = self.character_dict[rand_key]
            username += arr[random.randrange(len(arr))]

        loader.star_loading('Generating username now..')
        print(color.red_back(
            '\n\nPlease make note of your generated username for logging in'))
        print(color.green_fore(
            f'\n\nUSERNAME: {username}'))
        result = input('\n\n\t\tAre you happy with this username? y/n :')
        if result in ('Y', 'y'):
            print(color.green_fore('Thank you'))
            time.sleep(2)
            clear_console()
        if result in ('N', 'n'):
            print(color.purple_fore(
                '\n\nSorry about that, let us try that again for you'))
            time.sleep(2)
            self._generate_username()
        return username

    def _set_user_password(self):
        """
        When called it sets the users password and validates the selected
        password for the given criteria. If the password is not valid it
        uses recursion in order to get a valid input.
        """
        clear_console()

        print('\n\n\n\nNow lets set a password for you.')
        print(color.cyan_fore('Please make sure to have the following: '))
        print('You need a password of at least 10 characters')
        print(color.red_fore('It must contain at least 1 number'))
        print(color.red_fore('It must also contain at least 1 capital letter'))
        print(color.red_fore(
            'It must contain at least 1 of the special symbols below'
            ))
        print(f'\n{self.special_chars}')
        print(color.yellow_fore(
            '\n\t**Please note for your protection password input is hidden**'
            ))
        password_one = getpass('\n\nEnter your password here: ')
        password_two = getpass('Enter your password again to confirm: ')

        if password_one == password_two:
            pass
        else:
            print(color.red_fore('PASSWORDS NOT MATCHING, try again.'))
            time.sleep(2)
            self._set_user_password()

        checker = True  # checker is true until proven invalid
        for char in password_one:
            if char not in self.alphabet and char not in self.special_chars:
                if char not in self.character_dict['a']:
                    checker = False
                    break

        if checker is False:
            print(color.red_fore('\n INVALID password chosen, try again'))
            time.sleep(2.5)
            self._set_user_password()  # used recursion until valid password

        if len(password_one) < 10:
            print('Password too short, please try again')

        return password_one

    def _save_user_credentials(self):
        """
        Saves a new users hashed password to a Mongo Database so
        the user can choose the login route for returning users.
        A new hash and salt are generated for each user. Increasing
        the security of the data.
        """
        try:
            new_user = {}
            new_user["_id": self.username]
            print('\n\nAccessing database now')
            loader.color_background(60, loader.cyan_back)
            time.sleep(2)
            self._password = bytes(
                self._password, 'utf-8')  # convert password to bytes
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(self._password, salt)
            new_user['password'] = f'{salt}:{hashed}'
            post = new_user
            self._collection.insert_one(post)
            loader.hash_loading('Storing user credentials')
        except Exception:
            print('Issues contacting database.. please wait')
            time.sleep(5)
            self._save_user_credentials()

    def _log_in_user(self):
        """
        Logs the user into Rapid Silver.
        """
        clear_console()
        try:
            file = open('assets/text/logging_in.txt', encoding='utf8')
            message = file.read()
            file.close()
            print(
                color.cyan_fore(message)
            )
        except IOError:
            print(
                color.red_fore('Welcome user')
            )

        try:
            self.username = input(color.blue_fore(
                'Enter your username here: '
                ))
            post = self._collection.find_one({"_id": f"{self.username}"})

            print(color.cyan_fore(
                '\n\t**Your password input is hidden**'
                ))
            self._password = getpass('Please enter your password here: ')
            check_pass = self._check_user_password_matches(
                post, self._password)
            if post is None:
                raise ValueError(
                    'Sorry username or passord incorrect'
                )
            if check_pass is None:
                raise ValueError(
                    'Sorry username or passord incorrect'
                )

        except ValueError as error:
            # Message is the same if username or password is incorrect
            print(f'INVALID: {error}..')
            time.sleep(3)
            self._log_in_user()
        except TypeError:
            # Message is the same if username or password is incorrect
            print('INVALID: Sorry username or passord incorrect')
            time.sleep(3)
            self._log_in_user()

    def _check_characters_valid_in(self, to_check, input_type):
        """
        Checks all the characters in the input type to see if any return
        false. Returns false if the input type contains symbols specified
        in the variables at the top of PasswordManager class.
        """
        result = True
        if to_check == 'username':
            for char in input_type:
                if char in self.special_chars:
                    return False
        return result

    def _check_user_password_matches(self, post, user_pass_input):
        """
        Checks to see if password hash matches stored hashed password
        in MonogoDB. Returns true if a match and none otherwise.
        """
        pass_dict = post['password']
        hashed_list = pass_dict.split(':')

        # using string method replace to remove the chars for encoding properly
        hashes = hashed_list[1]
        hashes = hashes.replace("b'", "")
        hashes = hashes.replace("'", "")
        hashed = bytes(hashes, 'utf-8')

        user_pass_input = bytes(user_pass_input, 'utf-8')
        if bcrypt.checkpw(user_pass_input, hashed):

            print("\n\nYou are now logged in")
            time.sleep(1)
            return True
        else:
            print('\n\nUsername or password incorrect, try again')
            time.sleep(3)
            clear_console()
            self.__init__('old')  # use recursion to check log in details

        return None

    def check_database_usernames(self, username):
        """
        Checks to see if name is available to the user.
        """
        result = self._collection.find_one({"_id": username})
        time.sleep(1)
        return result

    def get_user_name(self):
        """
        Returns the users username.
        """
        return self.username
