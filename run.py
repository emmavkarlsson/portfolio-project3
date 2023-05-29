import random
import constants
import graphic

def title_of_game():
    """
    Adds a title to the screen
    """
    print("Welcome to the HANGMAN game!")

def generate_random_word(words):
    """
    Generates a random word for the user to guess
    from the word list in constants.py
    """
    index = random.randint(0, len(constants.WORDS) - 1)
    return constants.WORDS[index]
    

def display_word(word):
    """
    Prints out the letters of the words
    as underscores
    """
    value = ""
    for i in range(len(word)):
        value += "_ "
    print(value)


#function below is used to test to see if the game works

def main():
    title_of_game()
    game_word = generate_random_word(constants.WORDS)
    print(game_word)
    display_word(game_word)

main()