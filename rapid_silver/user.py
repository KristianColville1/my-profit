"""Holds the user class for creating user objects"""

class User():
    """Creates a user object for the current user of the terminal"""
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    