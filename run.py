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
from rapid_silver.rapid_profile import RapidUser
from rapid_silver.art import TextArt


# class instances
COLOR = TextArt()
LOADING = COLOR  # used for loading animations

# global variables
INVALID = False


def welcome_msg():
    """
    Prints welcome text to the terminal. Helps direct the user and lead
    on to navigation options.
    """
    try:
        file = open('assets/text/welcome.txt', encoding='utf8')
        welcome = file.read()
        file.close()
    except IOError:
        return "Welcome to MyProf"  # in the event an error occurs
    return welcome


def open_login_portal():
    """
    When called it displays the log in screen to the terminal.
    Gets the user type. Sets up a new account for new users and
    logs in returning users. Calls login_user() or create_account()
    and assigns it to variable user.
    """
    try:
        clear_console()
        file = open('assets/text/login.txt', encoding='utf8')
        login_msg = file.read()
        file.close()
        print('\n' + COLOR.cyan_fore(login_msg))
    except IOError:
        print('Log in screen')  # in event reading log in message fails

    print(COLOR.green_fore("\n\t\t\tHit 'e + Enter' to login"))
    print(COLOR.yellow_fore("\t\t\tHit 'd + Enter' to create new account"))

    try:
        result = input(COLOR.green_fore('\n\t\t\tHere: '))
        if result not in ('e', 'd'):
            print(COLOR.red_fore('\t\t\tInvalid input, enter e or d'))
            time.sleep(2)
            clear_console()
            open_login_portal()
        if result == 'e':
            user = login_user()
            return user
        if result == 'd':
            user = create_account()
            return user
    except ValueError:
        open_login_portal()  # uses recursion until valid login input
    return None


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """
    # TODO: create log in code for user and return user
    print('\n\n')
    LOADING.money_loading('\t\tOpening login now')
    clear_console()
    user = RapidUser('old')  # rapid user runs route for returning user
    return user


def create_account():
    """
    When called it pulls up the log in for creating a user account.
    """
    print('\n\n')
    LOADING.money_loading('\t\tAccount creation enabled')
    clear_console()
    user = RapidUser('new')  # rapid user runs route for new user
    return user


def load_details():
    """
    At the beginning of the program this describes the purpose of the CLI
    application and what the intended functionality is.
    """
    clear_console()
    print('\n\n\n\n\n')
    print(COLOR.cyan_fore('\n\t\t\tAccessing internal database now.\n'))
    LOADING.star_loading('\t\t\tLoading results ')
    time.sleep(0.3)
    clear_console()
    print(COLOR.red_fore('\n\t\t\tWelcome to Rapid Silver\n\n'))
    try:
        file = open('assets/text/rapid_details.txt', encoding='utf8')
        details = file.read()
        print(COLOR.yellow_fore(details))
        input('\n\n\nHit enter to continue')
    except IOError:
        print(COLOR.red_fore("""
        \n\nOops.. fetching details failed, trying again."""))
        time.sleep(2.5)
        clear_console()
        load_details()


def get_options():
    """
    Displays available options to the user for the Rapid Silver
    CLI application.
    """
    clear_console()
    try:
        file = open('assets/text/options.txt', encoding='utf8')
        option_screen = file.read()
        file.close()
        print('\n\n' + COLOR.yellow_fore(option_screen) + '\n\n')
    except IOError:
        print(COLOR.yellow_fore('\t\t\tOptions\n\n\n\n'))
    # TODO: add options here for user


def main():
    """
    Runs the program.
    """
    print(COLOR.red_fore(welcome_msg()))

    input(COLOR.purple_fore('\n\n\n\t\t\t<Press enter to continue to log in>'))
    load_details()

    # gets or sets up a user profile
    user = open_login_portal()


main()
