import argparse
from typing import Literal

from config import LevelConfig

DifficultyLevel = Literal["easy", "normal", "hard"]
separator = "=== * === * === * ==="


def show_game_info(attempts: int, config: LevelConfig):
    print(separator)
    print(f"Current Attempt: {attempts}")
    print(f"Attempts Left: {config.max_attempts - attempts}")
    print(separator)


def show_game_title(difficulty: DifficultyLevel):
    print("=== WELCOME TO GUESS THE NUMBER ===")
    print(f"Difficulty: {difficulty}")


def show_winning_info():
    print(separator)
    print("CONGRATULATIONS! YOU WON")
    print(separator)


def get_difficulty_from_console() -> DifficultyLevel:
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

    args = parser.parse_args()
    return args.difficulty
