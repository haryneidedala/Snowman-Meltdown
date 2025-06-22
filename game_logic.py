# game_logic.py
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current game state including snowman stage and word progress."""
    # Show appropriate snowman stage
    print(STAGES[mistakes])
    
    # Display secret word with underscores for unguessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print(f"Mistakes: {mistakes}/{len(STAGES)-1}")
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))

def is_word_guessed(secret_word, guessed_letters):
    """Check if all letters in secret word have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    
    # Game state variables
    mistakes = 0
    guessed_letters = []
    max_mistakes = len(STAGES) - 1
    
    # Game loop
    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Get valid input
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter exactly one letter.")
            elif not guess.isalpha():
                print("Please enter a valid letter (a-z).")
            elif guess in guessed_letters:
                print("You've already guessed that letter.")
            else:
                break
        
        # Process new guess
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            print(f"Incorrect! '{guess}' is not in the word.")
            mistakes += 1
    
    # Final game state display
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Game outcome
    if is_word_guessed(secret_word, guessed_letters):
        print("Congratulations! You saved the snowman!")
    else:
        print("Oh no! The snowman melted completely!")
        print(f"The secret word was: {secret_word}")
