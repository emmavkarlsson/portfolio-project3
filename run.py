import random
import constants
import graphic

def title_of_game():
    """
    Adds a title to the screen
    """
    print("Welcome to the HANGMAN game!")

def generate_random_word(words):
    index = random.randint(0, len(constants.WORDS) - 1)
    return constants.WORDS[index]

