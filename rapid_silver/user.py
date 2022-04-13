"""Holds the user class for creating user objects"""
import time
from better_profanity import profanity
from rapid_silver.text_art import TextArt
from rapid_silver.password_manager import PasswordManager
from console import clear_console

# instance variables

color = TextArt()
loading = color  # used to differentiate semantics


class User():
    """
    Base class for users of Rapid Silver.
    """

    # instance variables initially set to None
    first_name = None
    last_name = None
    email = None
    company_name = None

    def __init__(self, account_type):
        if account_type == 'new':
            self.validation = PasswordManager(account_type)  # activates the password manager
        elif account_type == 'old':
            # only gets data if needed from user from password manager
            self.validation = PasswordManager(account_type)  # activates the password manager

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
            # checks if correct otherwise uses recursion
            self.check_if_correct(self.set_first_name, fname_input)
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
            # checks if correct otherwise uses recursion
            self.check_if_correct(self.set_last_name, lname_input)
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
            # checks if correct otherwise uses recursion
            self.check_if_correct(self.set_email, email_input)
            self.email = [f'{email_input}']
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_email()
          # wrapped in string as not showing otherwise
        return self.email

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
            # checks if correct otherwise uses recursion
            self.check_if_correct(self.set_company_name, company_input)
        except ValueError as error:
            clear_console()
            print(color.red_fore(f'{error}'))
            self.set_company_name()
        company_name = company_input
        return company_name

    def check_if_correct(self, caller, user_input):
        """
        Checks individual statements to see if user wants to correct
        their input.
        """
        clear_console()
        for_recursion = caller
        result = input(color.purple_fore(f'\nIs {user_input} correct? y/n'))
        if result in ('y', 'Y'):
            print(color.green_fore('\nThank you'))
            time.sleep(0.7)
            clear_console()
            return None
        if result in ('n', 'N'):
            print(color.yellow_fore('\nOkay try again'))
            time.sleep(0.7)
            clear_console()
            for_recursion()
        if result not in ('y', 'Y', 'n', 'N'):
            print(color.red_fore('Invalid input given.'))
            for_recursion()
        return None

    def check_if_all_correct(self):
        """
        Displays all the details to the user to confirm if all their
        inputs are correct before moving on with the program.
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
            print('Not to worry lets try that again.')
            time.sleep(1.5)
            clear_console()
            self.__init__('new')  # redo init if wrong
        if result in ('y', 'Y'):
            clear_console()
            print('Thank you')
            loading.star_loading('Storing your details for later')
        else:
            self.check_if_all_correct()  # incase user enters something else
