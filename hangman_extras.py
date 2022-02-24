import sys
import time


def typewriter(string):
    """
    Typewriter for the main sentence in the beginning of the game
    """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)