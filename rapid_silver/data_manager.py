"""
Data manager hold the DataManager Class for Rapid Silver.
Manages user data for a given user profile.
"""

class DataManager():
    """
    Manages user data and accesses the resources for the user when activated.
    Stores the users data entered. Updates the users data. It can only be used
    with the PasswordManagers credentials for the logged in user.
    """
    def __init__(self, user_id):
        self.user = user_id