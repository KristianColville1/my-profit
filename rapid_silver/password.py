"""Hold the password class for Rapid Silver"""
from getpass import getpass
from cryptography.fernet import Fernet


class PasswordManager:
    """
    Handles the password information for the user of
    Rapid Silver.
    """
    def __init__(self, account_type):
        if account_type == 'new':
            self.set_user_password()
            self.log_in_user()
        elif account_type == 'old':
            self.get_login_details()
            self.log_in_user()

    def set_user_password(self):
        return ''
    def log_in_user(self):
        return ''
    def get_login_details(self):
        return ''
    # TODO: Create salt, pepper and hashing
    # TODO: Store inside a database
    # TODO: block user password from being stored anywhere in plain text
    # TODO: get all code and structure it properly
