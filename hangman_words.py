import random

words = [
    "Lisbon",
    "Madrid",
    "Brazil",
    "Japan",
    "Dublin",
    "India",
    "Luanda",
    "Copenhagen",
    "Brazzaville",
    "Jakarta",
    "Amsterdam",
    "Thailand",
    "Turkmenistan",
    "Switzerland"
]


def get_word():
    """
    Get a random word from the words list
    """
    random_word = random.choice(words)
    return random_word.upper()
