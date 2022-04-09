"""Holds the user class for creating user objects"""


class User(object):
    """
    Base class for users of Rapid Silver.
    """
    name = str

    def __init__(self, name):
        self.name = name
