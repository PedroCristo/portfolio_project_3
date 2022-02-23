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
    print(F"{Fore.YELLOW}\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(f"""{Fore.YELLOW}\t
    YOU HAVE TO GUESS A WORD WITH {len(random_word)} LETTERS""")
    print(display_hangman(attempts))
    print(full_word)
    print("\n")  
    while not guessed and attempts > 0:
        print(f"{Fore.RED}\n\tWRONG LETTERS GUESSED:\n\t{guessed_wrong}\n")
        display_score()
        if attempts > 1:
            print(f"{Fore.YELLOW}\n\tYOU HAVE {attempts} attempts")
        else:
            print(f"{Fore.RED}\n\tYOU HAVE {attempts} ATTEMPT LEFT\n")
        guess = input(f"""{Fore.CYAN}\t\t
        GUESS A LETTER OR A WORD PLEASE:\n\t>>> """).upper()















