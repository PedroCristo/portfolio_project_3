import colorama
from colorama import Fore
colorama.init(autoreset=True)

stages = [
 """
 """,
 # hangaman torso, head, two arms and one leg
 Fore.RED +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|            _|_
                   |\/|           (O_O)
                   |/\|          ./|||\.
                   |\/|         ./ ||| \.
                   |/\|              \.
                   |\/|               \_
                   |/\|  D A N G E R   Z O N E
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # hangaman torso, head and two arms
 Fore.RED +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|            _|_
                   |\/|           (O_O)
                   |/\|          ./|||\.
                   |\/|         ./ ||| \.
                   |/\|
                   |\/|
                   |/\|  D A N G E R   Z O N E
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # hangaman torso, head and one arm
 Fore.YELLOW +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|            _|_
                   |\/|           (O_O)
                   |/\|          ./|||
                   |\/|         ./ |||
                   |/\|
                   |\/|
                   |/\|
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # hangman torso
 Fore.YELLOW +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|            _|_
                   |\/|           (O_O)
                   |/\|            |||
                   |\/|            |||
                   |/\|
                   |\/|
                   |/\|
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # hangman head
 Fore.GREEN +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|            _|_
                   |\/|           (O_O)
                   |/\|
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # hangman rope
 Fore.GREEN +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|             |
                   |/\|             |
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
 """,
 # initial hangman state
 Fore.GREEN +
 """
                 ___________________
                |/\/\/\/\/\/\/\/\/\/|
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
                   |/\|
                   |\/|
        ___________|/\|__________
        |/\/\/\/\/\/\/\/\/\/\/\/|
"""
]

hangman_logo = [
 # hangman logo
 """
                        ______________________
                        |/\/\/\/\/\/\/\/\/\/\/|
                             |/\|             |
                             |\/|            _|_
                             |/\|           (o_O)
                             |\/|          ./|||\.
                             |/\|         ./ ||| \.
  _______ _    _ ______      |\/|           ./ \.
 |__   __| |  | |  ____|     |/\|          _/   \_
    | |  | |__| | |__        |\/|
    | |  |  __  |  __|   ____|/\|___________________
    | |  | |  | | |____ |/\/\/\/\/\/\/\/\/\/\/\/\/\/|
  _ |_|_ |_|  |_|______| _____ __  __          _   _
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|

          WOULD YOU TAKE THE RISK TO PLAY?
""",
 # hangman lose game logo
 """
                        ______________________
                        |/\/\/\/\/\/\/\/\/\/\/|
                             |/\|             |
   Y O U    L O S E !!       |\/|            _|_
                             |/\|           (o_O)
                             |\/|          ./|||\.
                             |/\|         ./ ||| \.
  _______ _    _ ______      |\/|           ./ \.
 |__   __| |  | |  ____|     |/\|          _/   \_
    | |  | |__| | |__        |\/|
    | |  |  __  |  __|   ____|/\|___________________
    | |  | |  | | |____ |/\/\/\/\/\/\/\/\/\/\/\/\/\/|
  _ |_|_ |_|  |_|______| _____ __  __          _   _
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
""",
 # hangman win game logo
 """
                        ______________________
                        |/\/\/\/\/\/\/\/\/\/\/|
   Y O U    W I N !!         |/\|             |
                             |\/|             |
                             |/\|
                             |\/|            ___
                             |/\|           (O_O)
  _______ _    _ ______      |\/|          ./|||\.
 |__   __| |  | |  ____|     |/\|         ./ ||| \.
    | |  | |__| | |__        |\/|           ./ \.
    | |  |  __  |  __|   ____|/\|___________/___\___
    | |  | |  | | |____ |/\/\/\/\/\/\/\/\/\/\/\/\/\/|
  _ |_|_ |_|  |_|______| _____ __  __          _   _
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
""",
 # hangman extra win game logo
 """
                        ______________________
                        |/\/\/\/\/\/\/\/\/\/\/|
   Y O U    W I N !!         |/\|             |
                             |\/|             |
   5 0 0   E X T R A         |/\|
                             |\/|            ___
      P O I N T S            |/\|           (O_O)
  _______ _    _ ______      |\/|          ./|||\.
 |__   __| |  | |  ____|     |/\|         ./ ||| \.
    | |  | |__| | |__        |\/|           ./ \.
    | |  |  __  |  __|   ____|/\|___________/___\___
    | |  | |  | | |____ |/\/\/\/\/\/\/\/\/\/\/\/\/\/|
  _ |_|_ |_|  |_|______| _____ __  __          _   _
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
"""
]

game_info = [
 # hangman game rules
 """
    _________________________________________________________________________
   |   ___________________________________________________________________   |
   |  |                                                                   |  |
   |  |                ===============================                    |  |
   |  |                | |                         | |                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                | |                         | |                    |  |
   |  |                ===============================                    |  |
   |  |                                                                   |  |
   |  |  1 - You have 7 attempts to try to find the right word by         |  |
   |  |      inputting letters or the full word                           |  |
   |  |  2 - If you guess a wrong letter you will lose an attempt and the |  |
   |  |      hangman will begin building                                  |  |
   |  |  3 - When you reach 0 lives you will be hanged - Game Over        |  |
   |  |  POINTS:                                                          |  |
   |  |  * 25 points per letter guessed right                             |  |
   |  |  * 200 points if you guessed the right word                       |  |
   |  |  * 500 extra points to complete the full word with max 3 letters  |  |
   |  |    already guessed.                                               |  |
   |  |___________________________________________________________________|  |
   |_________________________________________________________________________|
""",
 # hangman leaderbord
 """
    ============================================================

                      L E A D E R B O A R D

    ============================================================
    \tPOS\tNAME\t SCORE\t  DATA\t\tCITY
    ============================================================
"""
]
