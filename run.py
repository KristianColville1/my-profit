"""My Prof is tool businesses can use to calculate and forecast profits for their products"""
import time
from console import clear_console
from rapid_silver.c_print import ColorPrint
from rapid_silver.rapid_profile import RapidUser


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


def login_screen():
    """
    When called it displays the log in screen to the terminal.
    """
    color = ColorPrint()
    try:
        clear_console()
        file = open('login.txt')
        login_msg = file.read()
        file.close()
        print('\n' + color.p_cyan(login_msg))
    except IOError:
        # in event reading log in message fails
        print('Log in screen')

    print(color.p_yellow("\n\t\t\tHit 'e + Enter' to login"))
    print(color.p_yellow("\t\t\tHit 'd + Enter' to create new account"))


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """
    # TODO: create log in code for user and return user after account creation code finished
    return ''


def create_account():
    """
    When called it pulls up the log in for creating a user account.
    """
    clear_console()
    color = ColorPrint()
    try:
        file = open('new_account.txt', encoding='utf8')
        option_screen = file.read()
        file.close()
        print('\n\n'+ color.p_yellow(option_screen) + '\n\n')
    except IOError:
        print(color.p_yellow('\t\t\tOptions\n\n\n\n'))

    try:
        name = input(str(color.p_green('Enter your name here: ')))
        if len(name) < 3 or len(name) > 15:
            raise ValueError()
    except ValueError:
        print(color.p_red('WARNING: Name must be more than 3 characters and max 15'))
        time.sleep(3)
        clear_console()
        create_account()

    user = RapidUser(name)
    return user


def get_options():
    """
    Displays available options to the user for the Rapid Silver
    CLI application.
    """
    clear_console()
    color = ColorPrint()
    try:
        file = open('options.txt', encoding='utf8')
        option_screen = file.read()
        file.close()
        print('\n\n'+ color.p_yellow(option_screen) + '\n\n')
    except IOError:
        print(color.p_yellow('\t\t\tOptions\n\n\n\n'))
    # TODO: add options here for user


def get_user_type():
    """
    Gets the user type. Sets up a new account for new users and
    logs in returning users. Calls login_user() or create_account()
    and assigns it to variable user.
    """
    color = ColorPrint()
    try:
        result = input(color.p_green('\n\t\t\tHere: '))
        if result not in ('e', 'd'):
            print(color.p_red('\t\t\tInvalid input, enter e or d'))
            time.sleep(2.5)
            clear_console()
            login_screen()
    except ValueError:
        login_screen()
    if result == 'e':
        user = login_user()
    elif result == 'd':
        user = create_account()
    return user


def main():
    """
    Runs the program.
    """
    color = ColorPrint()
    print(color.p_red(welcome_msg()))
    input(color.p_yellow('\n\n\n\t\t< Press enter to continue to log in >'))
    login_screen()
    # gets or sets up a user profile
    user = get_user_type()


main()
