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
from rapid_silver.password_manager import PasswordManager
from rapid_silver.user import User
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
            login = login_user()
            return login
        if result == 'd':
            login = create_account()
            return login
        if result == 'b':
            pull_up_data_protection()
            open_login_portal()  # uses recursion until valid login input
    except ValueError:
        open_login_portal()  # uses recursion until valid login input
    except TypeError:
        open_login_portal()  # uses recursion until valid login input
    return login


def login_user():
    """
    When called it pulls up the log in screen for the user.
    """
    # TODO: create log in code for user and return user
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
        print(COLOR.purple_back(
            COLOR.yellow_fore(data_protection)
        ))
        print(COLOR.reset_bg)
    except IOError:
        print("ERROR: reading dataprotection failed..")
        print('We are GDPR compliant')

    input(COLOR.red_fore('\t\tHit enter to go back to log in portal'))


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

    try:
        file = open('assets/text/rapid_details.txt', encoding='utf8')
        messages = file.read()
        file.close()
        print(
            COLOR.green_fore(messages)
        )
    except IOError:
        print('Reading options failed.. Trying again.')
        time.sleep(1.5)
        get_options()


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
            '\t\tRapid Silver is business utility tool for the following:'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ a ] + Enter for > Setting up products'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ s ] + Enter for > Setting up  a mailing list'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ d ] + Enter for > Setting up employee lists'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ f ] + Enter for > Storing inventory/ updating inventory'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ g ] + Enter for > Analyzing inventory data'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ f ] + Enter for > Information on data protection'
        )
    )
    print(
        COLOR.yellow_fore(
            '\t\tHit [ g ] + Enter for > How data is stored and protected'
        )
    )


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
    open_selection_menu(validated_user)


main()
