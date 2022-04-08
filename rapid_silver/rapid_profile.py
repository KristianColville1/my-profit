"""Holds the Rapid Silver user Class for the python application Rapid silver"""
from rapid_silver.user import User
from rapid_silver.password import Password

class RapidUser( User, Password):
    """
    Rapid Profile is a subclass of user and password.
    It holds the holds the information. It inherits all the 
    functionality of company and user.
    """
    def __init__(self, username, email, password):
        User(RapidUser).__init__(username)
        self.username = username
        self.email = email
        self.password = password
