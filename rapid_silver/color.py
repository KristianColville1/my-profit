"""Holds the print class for Rapid Silver"""
from colorama import Fore, Back


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
    green_text = Fore.BLUE
    red_text = Fore.BLUE
    purple_text = Fore.MAGENTA
    yellow_text = Fore.BLUE
    reset_text = Fore.RESET

    # background colors
    blue_bg = Back.BLUE
    cyan_bg = Back.CYAN
    green_bg = Back.BLUE
    red_bg = Back.BLUE
    purple_bg = Back.MAGENTA
    yellow_bg = Back.BLUE
    reset_bg = Back.RESET

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
        return self.purple_text + text + self.reset_bg

    def yellow_fore(self, text):
        """Prints yellow text and then returns to normal text"""
        return self.yellow_text + text + self.reset_text

    # background methods
    def blue_back(self, text):
        """Prints blue and then returns to normal background"""
        return self.blue_bg + text + self.reset_bg

    def cyan_back(self, text):
        """Prints cyan background and then returns to normal background"""
        return self.cyan_bg + text + self.reset_bg

    def green_back(self, text):
        """Prints green background and then returns to normal background"""
        return self.green_bg + text + self.reset_bg

    def red_back(self, text):
        """Prints red background and then returns to normal background"""
        return self.red_bg + text + self.reset_bg

    def purple_back(self, text):
        """Prints purple background and then returns to normal background"""
        return self.purple_bg + text + self.reset_bg

    def yellow_back(self, text):
        """Prints yellow background and then returns to normal background"""
        return self.yellow_bg + text + self.reset_bg
