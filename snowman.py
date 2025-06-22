import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
    """
]

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

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    
    # Game state variables
    mistakes = 0
    guessed_letters = []
    
    # Initial game display
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Game loop
    while mistakes < len(STAGES) - 1:
        # Get user input
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        
        # Add new letter to guessed letters
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            
            # Check if guess is incorrect
            if guess not in secret_word:
                mistakes += 1
        
        # Update game display
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Temporary break for testing - remove in final version
        break

if __name__ == "__main__":
    play_game()
