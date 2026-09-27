"""
Number Guessing Game
IEEE LGU AI/ML Cohort One - Week 1 Assignment (Option 1)

The computer picks a secret random number between 1 and 100.
The player has a limited number of attempts to guess it correctly.
"""

import random


def get_valid_guess(low, high):
    """Ask the player for a guess and keep asking until it's a valid integer
    within the allowed range."""
    while True:
        user_input = input(f"Enter your guess ({low}-{high}): ")
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def choose_difficulty():
    """Let the player pick a difficulty level. Returns (low, high, attempts)."""
    print("\nChoose difficulty:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Hard   (1-200, 5 attempts)")
    print("3. Normal (1-100, 7 attempts)")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        return 1, 50, 10
    elif choice == "2":
        return 1, 200, 5
    else:
        return 1, 100, 7


def play_round():
    """Play a single round of the guessing game."""
    low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts_left = max_attempts
    guess_count = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_left > 0:
        guess = get_valid_guess(low, high)
        guess_count += 1
        attempts_left -= 1

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {guess_count} tries!")
            return True
        elif guess < secret_number:
            print(f"Too Low! Try a bigger number. ({attempts_left} attempts left)\n")
        else:
            print(f"Too High! Try a smaller number. ({attempts_left} attempts left)\n")

    print(f"\n😢 Out of attempts! The secret number was {secret_number}.")
    return False


def main():
    print("====================================")
    print("       NUMBER GUESSING GAME")
    print("====================================")

    wins = 0
    rounds_played = 0

    while True:
        won = play_round()
        rounds_played += 1
        if won:
            wins += 1

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break

    print("\n====================================")
    print("           FINAL SCORE")
    print("====================================")
    print(f"Rounds played: {rounds_played}")
    print(f"Rounds won:    {wins}")
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()
