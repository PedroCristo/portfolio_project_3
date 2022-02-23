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
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"""{Fore.YELLOW}\n\t
                YOU HAVE ALREADY GUESSED THIS LETTER {guess}\n""")
            elif guess not in random_word:
                print(f"""{Fore.RED}\n\t
                {guess} IS NOT IN THE WORD. TRY ANOTHER ONE!\n""")
                attempts -= 1
                guessed_letters.append(guess)
                guessed_wrong.append(guess)
            else:
                print(f"""{Fore.GREEN}\n\t
                GREAT, {guess} IS IN THE WORD! KEEP GOING!\n""")
                guessed_letters.append(guess)
                guessed_right += 1
                score += correct_guessed
                word_as_list = list(full_word)
                indices = [i for i, letter in enumerate(
                          random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True















