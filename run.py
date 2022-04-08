"""My Prof is tool businesses can use to calculate and forecast profits for their products"""
import time
from console import clear_console
from classes import c_print


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

def login_screen(color):
    """
    When called it displays the log in screen to the terminal.
    """
    try:
        clear_console()
        file = open('login.txt')
        login_msg = file.read()
        print('\n' + color.p_cyan(login_msg))
    except IOError:
        # in event reading log in message fails
        print('Log in screen')

    print(color.p_yellow("\n\t\t\tHit 'e + Enter' to login"))
    print(color.p_yellow("\t\t\tHit 'd + Enter' to create new account"))

    try:
        result = input(color.p_green('\n\t\t\tHere: '))
        if result not in ('e', 'd'):
            print(color.p_red('\t\t\tInvalid input, enter e or d'))
            time.sleep(2.5)
            login_screen(color)
    except ValueError:
        login_screen(color)
    return result


def main():
    """
    Runs the program.
    """
    color = c_print.ColorPrint()
    print(color.p_red(welcome_msg()))
    input(color.p_yellow('\n\n\n\t\t< Press enter to continue to log in >'))
    result = login_screen(color)
    clear_console()
    print(result)

SIGNED_IN = False
main()
