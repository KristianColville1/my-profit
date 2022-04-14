"""Holds text art class for Rapid Silver"""
import time
from rapid_silver.color import ColorPrint


class TextArt(ColorPrint):
    """
    Creates text art objects for the terminal. Subclass of ColorPrint.
    Provides simple text animations for loading and updating content etc.
    """

    hash_sym = '#'
    dot_sym = '.'
    money_sym = '$'
    star_sym = '*'

    def dot_loading(self, text):
        """
        Uses carriage return to make a basic animation for dot symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """
        text = str(text)
        for _ in range(25):
            text += self.cyan_fore(self.dot_sym)
            print(f'{text}\r', end='')
            time.sleep(0.05)

    def hash_loading(self, text):
        """
        Uses carriage return to make a basic animation for hash symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """
        text = str(text)
        for _ in range(25):
            text += self.yellow_fore(self.hash_sym)
            print(f'{text}\r', end='')
            time.sleep(0.05)

    def money_loading(self, text):
        """
        Uses carriage return to make a basic animation for money symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """
        text = str(text)
        for _ in range(25):
            text += self.green_fore(self.money_sym)
            print(f'{text}\r', end='')
            time.sleep(0.05)

    def star_loading(self, text):
        """
        Uses carriage return to make a basic animation for dot symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """
        text = str(text)
        for _ in range(25):
            text += self.purple_fore(self.star_sym)
            print(f'{text}\r', end='')
            time.sleep(0.05)

    def color_background(self, length, color):
        """
        Prints blank space to background but with color background for
        the length and color specified.
        """
        space = color + ' '
        for _ in range(length):
            space += color + ' '
            print(f'{space}\r', end='')
            time.sleep(0.02)
        print(self.reset_bg)
