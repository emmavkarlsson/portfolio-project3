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

def display_hangman(lives_left):
    """
    Displays the hangman graphics
    """
    current_graphic = len(graphic.HANGMAN) - lives_left - 1
    print(graphic.HANGMAN[current_graphic])
    

def display_word(word, guessed_letters):
    """
    Prints out the letters of the words
    as underscores
    """
    value = ""
    for i in range(len(word)):
        if word[i] in guessed_letters:
            value += word[i] + " "
        else: 
            value += "_ "
    print(value)

def display_lives(lives):
    """
    Displays how many lives the user has left
    """
    print("")
    print(f"Lives left: {lives}")


def display_guessed_letters(letters):
    """
    Displays the letters the user has already guessed
    """
    value = ""
    for i in letters:
        value += i + " "
    print(f"Guessed letters: {value}")
    print("")


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
            print("")
        elif guess not in constants.ALPHABET:
            print("Please enter a valid letter!")
            print("")
        elif guess in excluded_letters:
            print(f"You already guessed {guess}!")
            print("")
        else: 
            return guess


def check_guess(word, letter):
    """
    Checks how many times the guessed letter
    appears in the word
    """
    count_letter = word.count(letter)
    return count_letter


def main():
    guessed_letters = [] 
    lives_left = 6
    correct_answers = 0

    game_word = generate_random_word(constants.WORDS)

    while True:
        print("\033[H\033[2J", end="")
        title_of_game()
        display_hangman(lives_left)
        display_word(game_word, guessed_letters)
        display_lives(lives_left)
        display_guessed_letters(guessed_letters)

        if lives_left == 0:
            print(f"You lost! the word was '{game_word}'")
            return
        if correct_answers == len(game_word):
            print("You won!")
            return

        guess = get_and_validate_guess(guessed_letters)
        guessed_letters.append(guess)

        correct_guess = check_guess(game_word, guess)
        if correct_guess == 0:
            lives_left -= 1
        else:
            correct_answers += correct_guess


def play_again():
    """
    Gives the user the option to play again after they have won
    or lost. Accepts y and anything that starts with y as "yes".
    """
    return input("Do you want to play again? (y/n): ").lower().startswith("y")


if __name__ == '__main__':
    while True:
        main()
    
        if not play_again():
            break