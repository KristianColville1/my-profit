"""Holds text art class for Rapid Silver"""
import time
from rapid_silver.c_print import ColorPrint


class TextArt(ColorPrint):
    """
    Creates text art objects for the terminal. Subclass of ColorPrint.
    Provides simple text animations for loading and updating content etc.
    """

    hash_sym = '#'
    dot_sym = '.'
    money_sym = '$'

    def dot_loading(self):
        """
        Uses carriage return to make a basic animation for dot symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """

        text = 'Loading'
        for _ in range(15):
            text += self.p_cyan(self.dot_sym)
            print(f'{text}\r', end='')
            time.sleep(0.1)

    def hash_loading(self):
        """
        Uses carriage return to make a basic animation for hash symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """

        text = 'Loading'
        for _ in range(15):
            text += self.p_yellow(self.hash_sym)
            print(f'{text}\r', end='')
            time.sleep(0.1)

    def money_loading(self):
        """
        Uses carriage return to make a basic animation for money symbols.
        Used to add more visually pleasing terminal. Acts as a time delay
        between getting and setting data.
        """

        text = 'Loading'
        for _ in range(15):
            text += self.p_green(self.money_sym)
            print(f'{text}\r', end='')
            time.sleep(0.1)
