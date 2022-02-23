import random
import gspread


from hangman_words import *





def get_word():
    """
    Get a random word from the word list in hangman_words.py
    """
    random_word = random.choice(words)
    return random_word.upper()













