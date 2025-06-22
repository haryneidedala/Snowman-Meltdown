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
    # Clear screen for better readability
    print("\033c", end="")  # Clear terminal (works on most systems)
    
    # Show appropriate snowman stage with border
    print("=" * 40)
    print("SNOWMAN STATUS:")
    print(STAGES[mistakes])
    print("=" * 40)
    
    # Display secret word with formatting
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += f"\033[1;32m{letter}\033[0m "  # Green for correct
        else:
            display_word += "_ "
    
    print(f"\nWORD: {display_word.strip()}")
    print(f"Mistakes: {mistakes}/{len(STAGES)-1}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 40)

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
                guess = input("Guess a letter: ").strip().lower()
                if len(guess) != 1:
                    print("Please enter exactly one character.")
                elif not guess.isalpha():
                    print("Please enter a letter from A-Z.")
                elif guess in guessed_letters:
                    print("You've already guessed that letter. Try another.")
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
