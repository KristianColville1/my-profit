"""Holds the print class for MyProf"""

from colorama import Fore


class ColorPrint:
    """
    When created it allows calls to its various methods for
    printing in different colors of text to the terminal.
    Provides a more visually appealing program.
    """

    blue = Fore.BLUE
    cyan = Fore.CYAN
    green = Fore.GREEN
    red = Fore.RED
    yellow = Fore.YELLOW
    reset = Fore.RESET

    def __init__(self):
        self.name = 'Color Printer'

    def print_blue(self, text):
        """Prints text blue and then returns to normal text"""