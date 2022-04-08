"""Holds console command for clearing terminal screen"""
import os

# take from https://www.delftstack.com/howto/python/python-clear-console/
def clear_console():
    """Clears the console in the terminal"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
