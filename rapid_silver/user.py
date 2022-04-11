"""Holds the user class for creating user objects"""
import random
from profanity import profanity
from rapid_silver.color import ColorPrint
from rapid_silver.password import PasswordManager
from console import clear_console

# instance variables
color = ColorPrint()


class User(object):
    """
    Base class for users of Rapid Silver.
    """
    character_dict = {
        'a': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'b': ['R', 'A', 'P', 'I', 'D'],
        'c': ['S', 'I', 'L', 'V', 'E', 'R'],
        'd': ['M', 'O', 'N', 'E', 'Y'],
        'e': ['M', 'A', 'K', 'E', 'R'],
        'f': ['C', 'O', 'D', 'E'],
        'g': ['E', 'V', 'E', 'R', 'Y'],
        'h': ['D', 'A', 'Y']
    }

    character_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, account_type):
        if account_type is 'new':
            self.first_name = self.set_first_name()
            self.last_name = self.set_last_name()
            self.email = self.set_email()
            self.company_name = self.set_company_name()
            self.check_if_all_correct()
            PasswordManager(account_type)  # activates the password manager
        elif account_type is 'old':
            PasswordManager(account_type)  # activates the password manager

    def create_user_code_name(self):
        """
        Gives the user a Rapid user name code
        """
        rand_name = ''

        while len(rand_name) < 8:
            rand_key = self.character_keys[random.randrange(4)]
            arr = self.character_dict[rand_key]
            rand_name += arr[random.randrange(len(arr))]

        return rand_name

    def set_first_name(self):
        """Gets and validates the users first name"""
        first_name = ''
        try:
            text = color.yellow_fore('\nEnter your first name: ')
            fname_input = input(text)
            if len(fname_input) < 2 or len(fname_input) > 12:
                raise ValueError(
                    'First name must be between 3 and 12 characters'
                    )
            if profanity.contains_profanity(fname_input):
                raise ValueError(
                    'PROFANITY DETECTED. Try again.'
                )
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_first_name()
        first_name = fname_input
        return first_name

    def set_last_name(self):
        """Gets and validates the users last name"""
        last_name = ''
        try:
            text = color.yellow_fore('\nEnter your last name: ')
            lname_input = input(text)
            if len(lname_input) < 2 or len(lname_input) > 12:
                raise ValueError(
                    'Last name must be between 3 and 12 characters'
                    )
            if profanity.contains_profanity(lname_input):
                raise ValueError(
                    'PROFANITY DETECTED. Try again.'
                )
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_last_name()
        last_name = lname_input
        return last_name

    def set_email(self):
        """Gets and validates the users email"""
        email = ''
        try:
            text = color.cyan_fore('\nEnter your email: ')
            email_input = input(text)
            if '@' not in email_input:
                raise ValueError(
                    "You must have a '@' in your email address"
                    )
            if '.' not in email_input:
                raise ValueError(
                    "You must have a domain in your email i.e '.com'"
                    )
            if profanity.contains_profanity(email_input):
                raise ValueError(
                    'PROFANITY DETECTED. Try a different email address.'
                )
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_email()
        email = email_input
        return email

    def set_company_name(self):
        """Gets and validates the user company name"""
        company_name = ''
        try:
            text = color.yellow_fore('\nEnter your company name: ')
            company_input = input(text)
            if len(company_input) < 2 or len(company_input) > 12:
                raise ValueError(
                    'Company name must be between 3 and 12 characters'
                    )
            if profanity.contains_profanity(company_input):
                raise ValueError(
                    'PROFANITY DETECTED. Try again.'
                )
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_last_name()
        company_name = company_input
        return company_name

    def check_if_all_correct(self):
        """
        Displays the details to the user to confirm.
        """
        clear_console()
        print('Here are the details you provided: \n')
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.company_name)
        to_input = color.red_fore('Are these are all correct? y/n :')
        result = input(to_input)
        if result in ('n', 'N'):
            self.check_if_all_correct()
        if result in ('y', 'Y'):
            print('Thank you')
    # TODO: complete getter methods on data hookup
