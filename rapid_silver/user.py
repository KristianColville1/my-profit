"""Holds the user class for creating user objects"""
import random
from profanity import profanity
from rapid_silver.color import ColorPrint
from console import clear_console

# instance variables
color = ColorPrint()


class User(object):
    """
    Base class for users of Rapid Silver.
    """
    character_dict = {
        'a':['0', '1', '2', '3', '4', '5', '6', '7', '8','9'],
        'b':['R', 'A', 'P', 'I', 'D'],
        'c':['S', 'I', 'L', 'V', 'E', 'R'],
        'd':['M', 'O', 'N', 'E', 'Y'],
        'e':['M', 'A', 'K', 'E', 'R'],
        'f':['C', 'O', 'D', 'E'],
        'g':['E', 'V', 'E', 'R', 'Y'],
        'h':['D', 'A', 'Y']
    }

    character_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, account_type):
        if account_type == 'new':
            self.first_name = self.set_first_name()
            self.last_name = self.set_last_name()
            self.email = self.set_email()
            self.company_name = self.set_company_name()
        elif account_type == 'old':
            self.first_name = self.get_first_name()
            self.last_name = self.get_last_name()
            self.email = self.get_email()
            self.company_name = self.get_company_name()

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
            fname_input = input('Enter your first name')
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
        return ''

    def set_email(self):
        """Gets and validates the users email"""
        return ''

    def set_company_name(self):
        """Gets and validates the user company name"""
        return ''

