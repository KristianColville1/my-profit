"""Hold the password class for Rapid Silver"""
import gspread
from google.oauth2.service_account import Credentials


class Password(User):
    """
    Creates a password object for the user.
    """
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
    
    def __init__(self, password):
        self.password = password()
    
    
    def get_password(self):
        return ''