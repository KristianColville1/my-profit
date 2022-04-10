"""Holds the Rapid Silver user Class for the python application Rapid silver"""
from rapid_silver.user import User


class RapidUser(User):
    """
    Rapid Profile is a subclass of User.
    It inherits all the functionality of User.
    """
    def _check_user_database(self, name):
        """
        Checks database for name conflicts and returns True
        or False if name already exists.
        """
        data = name
        return data