"""
Rapid Silver is a mini business utility tool for users who are self-employed,
freelancers, or for small to medium sized businesses users. They can use this
tool too calculate and forecast profits for their products,
create mailing lists, send emails, create an organization structure,
design employee spread sheets
etc.
"""
import sys
import time
from console import clear_console
from rapid_silver.password_manager import PasswordManager
from rapid_silver.data_manager import DataManager
from rapid_silver.text_art import TextArt

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
        return "Welcome to Rapid Silver"  # in the event an error occurs
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
        print('\n' + COLOR.blue_fore(login_msg))
    except IOError:
        print('Log in screen')  # in event reading log in message fails

    print(COLOR.yellow_fore(
        "\n\t\tHit [ e ] + Enter to login"))
    print(COLOR.yellow_fore(
        "\t\tHit [ d ] + Enter to create new account"))
    print(COLOR.yellow_fore(
        "\t\tHit [ b ] + Enter to read how your data is stored"))

    try:
        result = input(COLOR.green_fore('\n\t\tHere: '))
        if result not in ('e', 'd', 'b'):
            print(COLOR.red_fore('\t\tInvalid input, enter e or d'))
            time.sleep(2)
            clear_console()
            open_login_portal()
        if result == 'e':
            user = login_user()
            return user
        if result == 'd':
            user = create_account()
            return user
        if result == 'b':
            pull_up_data_protection()
            input(COLOR.red_fore('\t\tHit Enter to go back to log in portal'))
            open_login_portal()  # uses recursion until valid login input
    except ValueError:
        open_login_portal()  # uses recursion until valid login input
    except TypeError:
        open_login_portal()  # uses recursion until valid login input


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """
    print('\n\n')
    LOADING.money_loading('\t\tOpening login now')
    clear_console()
    to_login = PasswordManager('old')  # runs route for new user
    return to_login


def create_account():
    """
    When called it pulls up the log in for creating a user account.
    """
    print('\n\n')
    LOADING.money_loading('\t\tAccount creation enabled')
    clear_console()
    to_login = PasswordManager('new')  # runs route for new user
    return to_login


def pull_up_data_protection():
    """
    Opens data protection information for the user to look at.
    Reassures user of entering sensitive information and logging in.
    """
    try:
        clear_console()
        file = open('assets/text/data_protection.txt', encoding='utf8')
        data_protection = file.read()
        file.close()
        print(
            COLOR.cyan_fore(data_protection)
        )
    except IOError:
        print("ERROR: reading dataprotection failed..")
        print('We are GDPR compliant')


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
        input('\n\n\n\t\t\t\tHit enter to continue')
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


def open_selection_menu(validated_user):
    """
    Once a user is logged in and validated the main route menu
    is shown and available options are displayed to the user.
    """
    clear_console()
    user = validated_user

    get_options()
    print(
        COLOR.red_fore(
            '\tAvailable options:'
        )
    )
    print(
        COLOR.yellow_fore(
            '\n\tHit [ q ] + Enter for > Set up user profile'
        )
    )
    print(
        COLOR.yellow_fore(
            '\tHit [ w ] + Enter for > To do list'
        )
    )
    print(
        COLOR.yellow_fore(
            '\tHit [ f ] + Enter for > Storing inventory/ updating inventory'
        )
    )
    print(
        COLOR.yellow_fore(
            '\tHit [ h ] + Enter for > Information on data protection'
        )
    )
    print(
        COLOR.yellow_fore(
            '\tHit [ i ] + Enter for > How data is stored and protected'
        )
    )
    print(
        COLOR.cyan_fore(
            '\tHit [ e ] + Enter for > Logging out and closing Rapid Silver'
        )
    )
    try:
        result = input(
            COLOR.green_fore('\n\t\tEnter here: ')
        )
        if result not in ('q', 'w', 'f', 'h', 'i', 'e'):
            raise ValueError(
                'INVALID INPUT. Try again.'
            )
        if result is TypeError:
            raise TypeError(
                'INVALID INPUT. Try again.'
            )
    except ValueError as error:
        print(
            COLOR.red_fore(f'{error}')
        )
        open_selection_menu(validated_user)  # recursion until valid
    except TypeError as error:
        print(
            COLOR.red_fore(f'{error}')
        )
        open_selection_menu(validated_user)  # recursion until valid

    if result == 'q':
        set_up_profile(user)
    elif result == 'w':
        set_up_to_do_list(user)
    elif result == 'f':
        store_update_stock_for(user)
    elif result == 'h':
        pull_up_data_protection()
        input(COLOR.red_fore('\t\tHit enter to go back to selection menu'))
        open_selection_menu(validated_user)  # recursive call to back to menu
    elif result == 'i':
        clear_console()
        explain_data_storage_to(validated_user)
        input(COLOR.yellow_fore('\t\tHit enter to go back to selection menu'))
        open_selection_menu(validated_user)  # recursive call to back to menu
    elif result == 'e':
        clear_console()
        sys.exit()


def set_up_profile(validated_user):
    """
    Sets up a logged in users profile and returns to the selection menu.
    """
    clear_console()
    print('\n\n\n\n\nLets check to see if you have a profile first.')
    LOADING.star_loading('Checking for user profile')
    DataManager(validated_user.username, 'profile')  # opens the data manager
    time.sleep(2)
    open_selection_menu(validated_user)


def set_up_to_do_list(validated_user):
    """
    The user can set up or update their to do list.
    """
    clear_console()
    LOADING.hash_loading('Checking for to do list now')
    DataManager(validated_user.username, 'to_do')  # opens the data manager
    time.sleep(2)
    open_selection_menu(validated_user)


def store_update_stock_for(validated_user):
    """
    Sets up a logged in users profile and returns to the selection menu.
    """
    clear_console()
    LOADING.money_loading('Checking your inventory now')
    DataManager(validated_user.username, 'inventory')  # opens the data manager
    time.sleep(2)
    open_selection_menu(validated_user)


def explain_data_storage_to(validated_user):
    """
    Sets up a logged in users profile and returns to the selection menu.
    """
    try:
        file = open('assets/text/data_storage.txt', encoding='utf8')
        data_notice = file.read()
        file.close()
        print(
            COLOR.red_fore(
                data_notice
            )
        )
    except IOError:
        print('Oops an error has occurred')
        time.sleep(2)
        print('Fetching files again.')
        print('Please wait')
        open_selection_menu(validated_user)


def main():
    """
    Runs the program.
    """
    # Add some new lines before loader
    for _ in range(5):
        print('\n')
    LOADING.hash_loading('\t\tLoading terminal for Rapid Silver')
    clear_console()

    # Load welcome message and login screen
    print(COLOR.red_fore(welcome_msg()))
    input(COLOR.cyan_fore('\n\n\n\t\t\t<Press enter to continue to log in>'))

    load_details()
    clear_console()
    LOADING.star_loading('Opening login portal now')
    # gets or sets up a user profile
    validated_user = open_login_portal()
    clear_console()

    # once user has either created an account or returned
    # they will have to log in
    # brings the user to all the available options and its the last call
    # in the main function.
    # user can navigate back to the selection menu from all of the available
    # options
    open_selection_menu(validated_user)


main()
