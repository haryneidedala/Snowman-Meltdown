# game_logic.py
import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Select a random word from the predefined list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display current game state including snowman stage and word progress."""
    # Display snowman stage
    print("\n" + "=" * 40)
    print(f"Snowman Status (Mistakes: {mistakes}/{MAX_MISTAKES})")
    print(STAGES[mistakes])
    print("=" * 40)
    
    # Display word progress
    display_word = " ".join(
        letter if letter in guessed_letters else "_" 
        for letter in secret_word
    )
    print(f"\nWord: {display_word}")
    
    # Display guessed letters
    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 40)


def validate_guess(guess, guessed_letters):
    """Validate user input and return error message if invalid."""
    if len(guess) != 1:
        return "Please enter exactly one letter."
    if not guess.isalpha():
        return "Please enter a valid letter (a-z)."
    if guess in guessed_letters:
        return "You've already guessed that letter."
    return None


def is_word_guessed(secret_word, guessed_letters):
    """Check if all letters in the secret word have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def get_user_guess(guessed_letters):
    """Prompt user for a valid letter guess."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()
        error = validate_guess(guess, guessed_letters)
        if not error:
            return guess
        print(f"Invalid input: {error}")


def play_game():
    """Main game loop for Snowman Meltdown."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    
    print("\n" + "=" * 40)
    print("Welcome to Snowman Meltdown!")
    print("Save the snowman by guessing the secret word!")
    print("=" * 40)
    
    # Game loop
    while mistakes < MAX_MISTAKES and not is_word_guessed(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_user_guess(guessed_letters)
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"\nCorrect! '{guess}' is in the word.")
        else:
            print(f"\nIncorrect! '{guess}' is not in the word.")
            mistakes += 1
    
    # Final game state
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Game outcome
    if is_word_guessed(secret_word, guessed_letters):
        print("\n🎉 Congratulations! You saved the snowman! 🎉")
    else:
        print("\n☃️ Oh no! The snowman melted completely! ☃️")
        print(f"The secret word was: {secret_word}")
