"""My Prof is tool businesses can use to calculate and forecast profits for their products"""
from console import clear_console
from classes import c_print
import time

def welcome_msg():
    """
    Prints welcome text to the terminal. Helps direct the user and lead
    on to navigation options.
    """
    try:
        file = open('welcome.txt', encoding='utf8')
        welcome = file.read()
        file.close()
    except IOError:
        # in the event an error occurs
        return "Welcome to MyProf"
    return welcome


def main():
    """
    Runs the program.
    """
    text = c_print.ColorPrint()
    print(text.print_red(welcome_msg()))
    input(text.print_yellow('\n\t\t\t< Press enter to continue to log in >'))

main()
