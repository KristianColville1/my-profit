"""
Rapid Silver is a mini business utility tool for users who are self-employed,
freelancers, or for small to medium sized businesses users. They can use this
tool too calculate and forecast profits for their products,
create mailing lists, send emails, create an organization structure,
design employee spread sheets
etc.
"""
import time
from console import clear_console
from rapid_silver.c_print import ColorPrint
from rapid_silver.rapid_profile import RapidUser
from rapid_silver.art import TextArt


# class instances
COLOR = ColorPrint()
LOADING = TextArt()

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
    try:
        clear_console()
        file = open('login.txt')
        login_msg = file.read()
        file.close()
        print('\n' + COLOR.p_cyan(login_msg))
    except IOError:
        # in event reading log in message fails
        print('Log in screen')

    print(COLOR.p_yellow("\n\t\t\tHit 'e + Enter' to login"))
    print(COLOR.p_yellow("\t\t\tHit 'd + Enter' to create new account"))


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """
    # TODO: create log in code for user and return user
    return ''


def create_account():
    """
    When called it pulls up the log in for creating a user account.
    """
    user = RapidUser()
    
    clear_console()
    LOADING.dot_loading()
    clear_console()
    try:
        file = open('new_account.txt', encoding='utf8')
        option_screen = file.read()
        file.close()
        print('\n\n' + COLOR.p_yellow(option_screen) + '\n\n')
    except IOError:
        print(COLOR.p_yellow('\t\t\tOptions\n\n\n\n'))

    try:
        name = input(str(COLOR.p_green('Enter your name here: ')))
        if len(name) < 3 or len(name) > 15:
            raise ValueError()
    except ValueError:
        print(COLOR.p_red('Name must be more than 3 characters and max 15'))
        time.sleep(3)
        create_account() # recursive call to get valid input

    user = RapidUser()
    return user


def get_options():
    """
    Displays available options to the user for the Rapid Silver
    CLI application.
    """
    clear_console()
    try:
        file = open('options.txt', encoding='utf8')
        option_screen = file.read()
        file.close()
        print('\n\n' + COLOR.p_yellow(option_screen) + '\n\n')
    except IOError:
        print(COLOR.p_yellow('\t\t\tOptions\n\n\n\n'))
    # TODO: add options here for user


def get_user_type():
    """
    Gets the user type. Sets up a new account for new users and
    logs in returning users. Calls login_user() or create_account()
    and assigns it to variable user.
    """
    try:
        result = input(COLOR.p_green('\n\t\t\tHere: '))
        if result not in ('e', 'd'):
            print(COLOR.p_red('\t\t\tInvalid input, enter e or d'))
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


def load_details():
    """
    At the beginning of the program this describes the purpose of the CLI
    application and what the intended functionality is.
    """
    clear_console()
    time.sleep(0.5)
    print('\n\n\n\n\n\t\t\t\r')
    LOADING.dot_loading()
    print(COLOR.p_blue('\n\nFetching resources......'))
    time.sleep(0.5)
    print(COLOR.p_cyan('\nAccessing internal database now.\n'))
    LOADING.hash_loading()
    time.sleep(0.3)
    clear_console()
    print(COLOR.p_red('\n\t\t\tWelcome to Rapid Silver\n\n'))
    try:
        file = open('rapid_details.txt', encoding='utf8')
        details = file.read()
        print(COLOR.p_yellow(details))
        input('\n\n\nHit enter to continue')
    except IOError:
        print(COLOR.p_red('\n\nOops.. fetching details failed, trying again.'))
        time.sleep(2.5)
        clear_console()
        load_details()


def main():
    """
    Runs the program.
    """
    print(COLOR.p_red(welcome_msg()))
    
    input(COLOR.p_yellow('\n\n\n\t\t< Press enter to continue to log in >'))
    load_details()
    login_screen()
    # gets or sets up a user profile
    user = get_user_type()


main()
