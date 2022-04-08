"""My Prof is tool businesses can use to calculate and forecast profits for their products"""
import time
from console import clear_console
from rapid_silver.c_print import ColorPrint

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
            clear_console()
            login_screen(color)
    except ValueError:
        login_screen(color)
    if result == 'e':
        login_user()
    elif result == 'd':
        create_account()


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """


def create_account():
    """
    When called it pulls up the log in for creating a user account.
    """


def main():
    """
    Runs the program.
    """
    color = ColorPrint()
    print(color.p_red(welcome_msg()))
    input(color.p_yellow('\n\n\n\t\t< Press enter to continue to log in >'))
    login_screen(color)



main()
