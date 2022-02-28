import datetime
import gspread
from google.oauth2.service_account import Credentials
from hangman_words import *
from hangman_art import *
from hangman_extras import *

import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

# Import date from datetime
date = datetime.datetime.today()
today_date = date.strftime("%d/%m/%Y")

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
E N T E R   Y O U R   N A M E\t\n\nA N D   G O O D   L U C K ! !\n""")

if __name__ == '__main__':

    # Allows the user to input their own name and city to play the game
    # Allows the user to input their own name and city to play the game
    while True:
        player_name = input(f"\n{Fore.CYAN}NAME:\n>>> ").strip().upper()
        if len(player_name) == 0:
            print(f"{Fore.RED}This is not a valid name!")
            continue
        else:
            break
    while True:
        player_city = input(f"{Fore.CYAN}YOUR CITY:\n>>> ").strip().upper()
        if len(player_city) == 0:
            print(f"{Fore.RED}This is not a valid city!")
            continue
        else:
            break
    print(f"""{Fore.YELLOW}\n\t
    HELLO {player_name}, WELCOME TO THE HANGMAN GAME!\n""")
    print(f"{Fore.BLUE}{game_info[0]}")
    input(f"""\n{Fore.CYAN}
    {player_name}, PRESS ANY KEY TO START THE GAME.\n    >>> """)

    # CONSTS
    CORRECT_GUESSED = 25
    EXTRA_SCORE = 100
    FULLY_WORD_SCORE = 500
    PLAY_AGAIN_MSG = f"""{Fore.CYAN}
    A - PLAY AGAIN     
    B - LEADERBOARD
    C - EXIT THE GAME
    """


def game(random_word):
    """
    Game main function
    """
    full_word = "_" * len(random_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    guessed_wrong = []
    guessed_right = 0
    attempts = 7
    score = 0
    print(F"{Fore.YELLOW}\n\tLET'S PLAY THE HANGMAN GAME!\n")
    print(f"""{Fore.YELLOW}\t
    YOU HAVE TO GUESS A WORD WITH {len(random_word)} LETTERS""")
    print(display_hangman(attempts))
    word_space(full_word)
    print("\n")
    while not guessed and attempts > 0:
        print(f"{Fore.RED}\n\tWRONG LETTERS GUESSED:\n\t{guessed_wrong}\n")
        display_score(score)
        print(f"""\n{Fore.CYAN}
        =================================================""")
        if attempts > 1:
            print(f"{Fore.YELLOW}\n\tYOU HAVE {attempts} ATTEMPTS")
        else:
            print(f"{Fore.RED}\n\tYOU HAVE {attempts} ATTEMPT LEFT\n")
        guess = input(f"""{Fore.CYAN}\t\t
        GUESS A LETTER OR A WORD PLEASE:\n\t>>> """).upper()
        print(f"""\n{Fore.CYAN}
        =================================================""")
        # Check if the player has already guess the letter
        # Or if the letter guessed in not in the word
        # And if the letter guessed is in the word
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
                score += CORRECT_GUESSED
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
        word_space(full_word)
        print("\n")
    final_result(guessed, random_word, guessed_right, score)


def final_result(guessed, random_word, guessed_right, score):
    """
    Check if the player won the game guessing the word letter
    by letter or the word at once or if the player loses the game
    """
    if guessed and len(random_word) >= 6 and guessed_right <= 3:
        print(f"{Fore.GREEN}{hangman_logo[3]}")
        print(f"""{Fore.GREEN}\n\t
        YOU WIN, {player_name} YOU HAVE GUESSED THE FULLY WORD AT ONCE!\n""")
        score = score + EXTRA_SCORE + FULLY_WORD_SCORE
    elif guessed:
        print(f"{Fore.GREEN}{hangman_logo[2]}")
        print(f"""{Fore.GREEN}\n\t
        YOU WIN, {player_name} YOU HAVE GUESSED THE RIGHT WORD!\n""")
        score = score + EXTRA_SCORE
    else:
        print(F"""{Fore.RED}\n\n\t
        YOU LOSE, {player_name} THE RIGHT WORD WAS {random_word}!""")
        print(f"{Fore.RED}{hangman_logo[1]}")
    update_worksheet(data, score)
    display_score(score)
    exit_menu()


def word_space(full_word):
    """
    Add space in between letters in the random word
    """
    for i in full_word:
        print(i, end=" ")


def display_hangman(attempts):
    """
    Display hangman stages from the start of the game
    and change anytime the player doesn't guess the right letter
    """
    return stages[attempts]


def display_score(score):
    """
    Display player score during the game
    """
    print(f"\tSCORE: {score}")


def update_worksheet(data, score):
    """
    Update a new row in the Hangman worksheet
    This updates a new row with the name, score and date.
    """
    print(f"\t{Fore.GREEN}Updating Leaderboard...\n")
    worksheet_to_update = SHEET.worksheet("leaderboard")
    worksheet_to_update.append_row([
      str(player_name[0:7]), score, today_date, player_city])
    print(f"\t{Fore.GREEN}Leaderboard Update successful.\n")


def display_leaderboard():
    """
   Displays the players leaderboard showing
   the 10 best scores
    """
    score_sheet = SHEET.worksheet("leaderboard").get_all_values()[1:]
    for data in score_sheet:
        data[1] = (data[1])

    update_data = sorted(score_sheet, key=lambda x: int(x[1]), reverse=True)

    print(f"{Fore.YELLOW}{game_info[1]}")
    if(len(update_data) < 15):
        count = len(update_data)
    else:
        count = 15

    for i in range(0, count):
        print(f"""
        {Fore.GREEN}{i+1}\t{update_data[i][0]}\t  {update_data[i][1]}\t{
        update_data[i][2]}\t{update_data[i][3]}""")
    print(f"""{Fore.YELLOW}\n
    ==============================================================""")


def exit_menu():
    """
    Give the player 3 choices in the end of any game.
    Play again, Leaderboard and Exit the game
    """
    while True:
        continue_playing = input(f"{PLAY_AGAIN_MSG}\n   >>>").lower()
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
            play_game = False
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














