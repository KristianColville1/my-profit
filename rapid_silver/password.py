"""Hold the password class for Rapid Silver"""
import gspread
from google.oauth2.service_account import Credentials
from cryptography.fernet import Fernet


class PasswordManager():
    """
    Handles the password information for the user of
    Rapid Silver.
    """
    
