from game_logic import play_game

def main():
    while True:
        play_game()
        replay = input("\nPlay again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
