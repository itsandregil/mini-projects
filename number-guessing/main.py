import argparse
import random

from config import levels


def get_answer() -> int:
    input_number = int(input("Pick a random number from 0 to 100: "))

    if input_number < 0 or input_number > 100:
        raise Exception("Number must be between 0 and 100")

    return input_number


def get_args_from_console():
    parser = argparse.ArgumentParser(
        prog="Random Number Guessing Game",
        description="The program will generate a random number and you will try to guess it",
    )
    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "normal", "hard"],
        default="normal",
        help="The difficulty level of the game",
    )

    return parser.parse_args()


def main():
    args = get_args_from_console()
    level_config = levels[args.difficulty]

    attempts = 0
    hidden_number = random.randint(0, level_config.upper_limit)

    while True:
        attempts += 1

        if attempts > level_config.max_attempts:
            print(f"Max attempts reached! You lost. Hidden number was {hidden_number}")
            break

        try:
            answer = get_answer()

            if answer == hidden_number:
                print("You won!")
                break
            elif answer > hidden_number:
                print("Pick a smaller number")
            else:
                print("Pick a bigger number")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
