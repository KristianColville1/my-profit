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


    def p_blue(self, text):
        """Prints text blue and then returns to normal text"""

        return self.blue + text + self.reset


    def p_cyan(self, text):
        """Prints text cyan  and then returns to normal text"""

        return self.cyan + text + self.reset


    def p_green(self, text):
        """Prints text green and then returns to normal text"""

        return self.green + text + self.reset


    def p_red(self, text):
        """Prints text red  and then returns to normal text"""

        return self.red + text + self.reset


    def p_yellow(self, text):
        """Prints text yellow and then returns to normal text"""

        return self.yellow + text + self.reset
