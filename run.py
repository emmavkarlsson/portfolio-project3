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


def display_guessed_letters(letters):
    """
    Displays the letters the user has already guessed
    """
    value = ""
    for i in letters:
        value += i + " "
    print(f"Guessed letters: {value}")


def get_and_validate_guess(excluded_letters):
    """
    Gets the guess from the user and validates it
    so it only returns if the user has entered
    one valid letter and a letter that hasn't 
    already been guessed
    """
    while True:
        guess = input("Guess a letter! ").lower()

        if len(guess) != 1:
            print("You can only enter 1 letter!")
        elif guess not in constants.ALPHABET:
            print("Please enter a valid letter!")
        elif guess in excluded_letters:
            print(f"You already guessed {guess}!")
        else: 
            return guess





#function below is used to test to see if the game works

def main():
    guessed_letters = [] 

    title_of_game()
    game_word = generate_random_word(constants.WORDS)

    while True:

        display_word(game_word)
        display_guessed_letters(guessed_letters)

        guess = get_and_validate_guess(guessed_letters)
        guessed_letters.append(guess)

    

main()