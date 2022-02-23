import random
import gspread


from hangman_words import *





def get_word():
    """
    Get a random word from the word list in hangman_words.py
    """
    random_word = random.choice(words)
    return random_word.upper()


def game(random_word):
    full_word = " " * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    guessed_wrong = []
    guessed right = 0
    attempts = 7
    score = 0
    correct_guessed = 25
    extra_score = 100
    fully_word_score = 500  













