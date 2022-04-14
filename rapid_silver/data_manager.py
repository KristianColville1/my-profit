"""
Data manager hold the DataManager Class for Rapid Silver.
Manages user data for a given user profile.
"""
import bcrypt
from pymongo import MongoClient
from console import clear_console
from rapid_silver.text_art import TextArt


class DataManager():
    """
    Manages user data and accesses the resources for the user when activated.
    Stores the users data entered. Updates the users data. It can only be used
    with the PasswordManagers credentials for the logged in user.
    """
    def __init__(self, user_id):
        self.user = user_id
        self.data_profile = None
    
    
    def _check_for_user_profile(self, profile):
        """
        """