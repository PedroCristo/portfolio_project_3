import random
# import gspread
from google.oauth2.service_account import Credentials


from hangman_words import *
from hangman_art import *
from hangman_extras import *
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')

leaderboard = SHEET.worksheet("leaderboard")

data = leaderboard.get_all_values()



print(f"{Fore.GREEN}{hangman_logo[0]}")
typewriter(f"""
Y O U   H A V E   A   P R E T T Y   N E C K   T O\t\n
P L A Y   T H I S   G A M E   B Y   T H E   W A Y ! !\t\n
E N T E R   Y O U R   N A M E\t\n\nA N D   G O O D   L U C K\n""")

if __name__ == '__main__':

    # Allows the user to input their own name to play the game
    while True:
        player_name = input(f"\n{Fore.CYAN}NAME:\n>>> ").strip().upper()
        player_city = input(f"YOUR CITY:\n>>> ").strip().upper()
        if len(player_name) > 0:
            break
    print(f"""{Fore.YELLOW}\n\t
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n""")
    print(f"{Fore.BLUE}{game_info[0]}")
    input(f"""\n{Fore.CYAN}
    {player_name}, PRESS ANY KEY TO START THE GAME.\n    >>> """)

def get_word():
    """
    Get a random word from the word list in hangman_words.py
    """
    random_word = random.choice(words)
    return random_word.upper()


def game(random_word):
    global full_word
    full_word = "_" * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    guessed_wrong = []
    global guessed_right
    guessed_right = 0
    attempts = 7
    global score
    score = 0
    correct_guessed = 25
    extra_score = 100
    fully_word_score = 500
    print(F"{Fore.YELLOW}\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(f"""{Fore.YELLOW}\t
    YOU HAVE TO GUESS A WORD WITH {len(random_word)} LETTERS""")
    print(display_hangman(attempts))
    word_space()
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
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print(f"""{Fore.YELLOW}\n\t
                YOU HAVE GUESSED THE WORD {guess} ALREADY.""")
            elif guess != random_word:
                print(f"{Fore.RED}\n\t{guess}, IS NOT THE WORD. TRY AGAIN!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                full_word = random_word
        else:
            print(f"{Fore.YELLOW}\n\tIS NOT VALID GUESS.\n")
        print(display_hangman(attempts))
        word_space()
        print("\n")
    if guessed and len(guess) > 2 and len(
       random_word) >= 6 and guessed_right <= 3:
        print(f"{Fore.GREEN}{hangman_logo[3]}")
        print(f"""{Fore.GREEN}\n\t
        YOU WIN, {player_name} YOU HAVE GUESSED THE FULLY WORD AT ONCE!\n""")
        score = score + extra_score + fully_word_score
    elif guessed:
        print(f"{Fore.GREEN}{hangman_logo[2]}")
        print(f"""{Fore.GREEN}\n\t
        YOU WIN, {player_name} YOU HAVE GUESSED THE RIGHT WORD!\n""")
        score = score + extra_score
    else:
        print(F"""{Fore.RED}\n\n\t
        YOU LOSE, {player_name} THE RIGHT WORD WAS {random_word}!""")
        print(f"{Fore.RED}{hangman_logo[1]}")
    display_score()
    exit_menu()  


def word_space():
    for i in full_word:
        print(i, end=" ")   


def display_hangman(attempts):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letter
    """
    return stages[attempts]



def display_score():
    """
    Display player score during the game
    """
    print(f"\tSCORE: {score}")

    
def update_worksheet(data):
    """
    Update a new row in the Hangman worksheet
    This updates a new row with the name, score and date.
    """
    print(f"\t{Fore.GREEN}Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet("leaderboard")
    worksheet_to_update.append_row([
      str(player_name[0:7]), score, today_date, player_city])
    print(f"\t{Fore.GREEN}Leaderboard Update successful.\n")



def exit_menu():
    """
    Give the player 3 choices in the end of any game.
    Play again, Leaderboard and Exit the game
    """
    while True:
        continue_playing = input(f"""{Fore.CYAN}\n\t
        A - PLAY AGAIN\t   B - LEADERBOARD\t C - EXIT THE GAME\n\t>>> """).lower()
        if continue_playing == "a":
            print(f"\n\tYou have decided to continue playing the game.\n")
            main()
        elif continue_playing == "b":
            display_leaderboard()
        elif continue_playing == "c":
            print(f"{Fore.RED}\n\tNow closing the game...")
            print(f"""{Fore.CYAN}
            \n\tThanks for playing, {player_name.capitalize()}.
            \n\tHope to see you again soon!\n""")
            sys.exit()
        else:
            print(f"""{Fore.YELLOW}\n\t
            That is not a valid option. Please try again.\n""")

def main():
    """
    Calls the get_word and game functions
    """
    random_word = get_word()
    game(random_word)
if __name__ == "__main__":

    main()              















