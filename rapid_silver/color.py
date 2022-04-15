"""Holds the print class for Rapid Silver"""
from colorama import Fore


class ColorPrint:
    """
    When created it allows calls to its various methods for
    printing in different colors of text to the terminal.
    Provides a more visually appealing program. Base class for
    TextPrint class.
    """

    # text colors
    blue_text = Fore.BLUE
    cyan_text = Fore.CYAN
    green_text = Fore.GREEN
    red_text = Fore.RED
    purple_text = Fore.MAGENTA
    yellow_text = Fore.YELLOW
    reset_text = Fore.RESET

    def __init__(self):
        self.name = 'Color Print Object'

    # text methods
    def blue_fore(self, text):
        """Prints text blue and then returns to normal text"""
        return self.blue_text + text + self.reset_text

    def cyan_fore(self, text):
        """Prints text cyan and then returns to normal text"""
        return self.cyan_text + text + self.reset_text

    def green_fore(self, text):
        """Prints text green and then returns to normal text"""
        return self.green_text + text + self.reset_text

    def red_fore(self, text):
        """Prints red text  and then returns to normal text"""
        return self.red_text + text + self.reset_text

    def purple_fore(self, text):
        """Prints purple text and then returns to normal text"""
        return self.purple_text + text + self.reset_text

    def yellow_fore(self, text):
        """Prints yellow text and then returns to normal text"""
        return self.yellow_text + text + self.reset_text
