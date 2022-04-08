"""Hold the password class for Rapid Silver"""

class Password():
    """
    Creates a password object for the user.
    """
    
    def __init__(self, password):
        self.password = password()
    
    
    def get_password(self):
        return ''