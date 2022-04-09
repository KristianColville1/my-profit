"""Holds the user class for creating user objects"""
import random

class User(object):
    """
    Base class for users of Rapid Silver.
    """
    character_dict = {
        'a':['0', '1', '2', '3', '4', '5', '6', '7', '8','9'],
        'b':['R', 'A', 'P', 'I', 'D'],
        'c':['S', 'I', 'L', 'V', 'E', 'R'],
        'd':['M', 'O', 'N', 'E', 'Y'],
        'e':['M', 'A', 'K', 'E', 'R'],
        'f':['C', 'O', 'D', 'E'],
        'g':['E', 'V', 'E', 'R', 'Y'],
        'h':['D', 'A', 'Y']
    }

    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


    def __init__(self):
        self.name = ''

    def create_rand_name(self):
        """
        Gives the user an option for generating a
        random username to use.
        """
        rand_name = ''

        while len(rand_name) < 12:
            rand_key = self.keys[random.randrange(4)]
            arr = self.character_dict[rand_key]
            rand_name += arr[random.randrange(len(arr))]

        return rand_name

