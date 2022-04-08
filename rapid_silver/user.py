"""Holds the user class for creating user objects"""

class User(object):
    """Creates a user object for the current user of the terminal"""
    
    def __init__(self, name):
        self.name = name

    