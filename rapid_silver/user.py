"""Holds the user class for creating user objects"""
import time
from better_profanity import profanity
from rapid_silver.text_art import TextArt
from console import clear_console

# instance variables

color = TextArt()
loading = color  # used to differentiate semantics


class User():
    """
    Base class for users of Rapid Silver.
    """

    def __init__(self):
        self.first_name = self.set_first_name()
        self.last_name = self.set_last_name()
        self.email = self.set_email()
        self.company_name = self.set_company_name()
        self.user_details = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Email": self.email,
            "Company": self.company_name
        }

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
        print('\n\n\n\n\n')
        result = input(color.cyan_fore(f"\n\tIs '{user_input}' correct? y/n: "))
        if result in ('y', 'Y'):
            print(color.yellow_fore('\nSaving'))
            loading.hash_loading('Saving')
            clear_console()
            return None
        if result in ('n', 'N'):
            print(color.green_fore('\nOkay try again'))
            time.sleep(0.7)
            clear_console()
            for_recursion()
        if result not in ('y', 'Y', 'n', 'N'):
            print(color.red_fore('Invalid input given.'))
            for_recursion()
        return None
