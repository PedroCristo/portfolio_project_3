import sys
import time


def typewriter(string):
    """
   Typewriter for the main sentence at the beginning of the game
   The Python code for the typewriter was taken from the following tutorial: [Kwasii](https://www.youtube.com/watch?v=A_1THfBpCH
   """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    