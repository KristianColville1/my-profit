"""Hold the password class for Rapid Silver"""
import gspread
from google.oauth2.service_account import Credentials

class Password(object):
    """
    Creates a password object for the user.
    """
    
    SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('rapid_silver')

    user_names = SHEET.worksheet('rapid_silver')
    data = user_names.get_all_values()
    def __init__(self, password):
        self.password = password


    def get_password(self):
        """"""