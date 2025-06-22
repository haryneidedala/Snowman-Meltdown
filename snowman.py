# snowman.py
from game_logic import play_game


def main():
    """Main entry point with replay functionality."""
    while True:
        play_game()
        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay not in ('y', 'yes'):
            print("\nThanks for playing Snowman Meltdown!")
            break
        print("\n" + "=" * 40 + "\nStarting new game...\n" + "=" * 40)


if __name__ == "__main__":
    main()
