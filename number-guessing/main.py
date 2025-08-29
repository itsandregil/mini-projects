import random

from config import LevelConfig, levels
from utils import (
    get_difficulty_from_console,
    show_game_info,
    show_game_title,
    show_winning_info,
)


def get_answer(config: LevelConfig) -> int:
    input_number = int(input(f"Pick a random number from 0 to {config.upper_limit}: "))

    if input_number < 0 or input_number > config.upper_limit:
        raise Exception(f"Number must be between 0 and {config.upper_limit}")

    return input_number


def main():
    difficulty = get_difficulty_from_console()
    level_config = levels[difficulty]

    attempts = 0
    hidden_number = random.randint(0, level_config.upper_limit)
    show_game_title(difficulty)

    while True:
        show_game_info(attempts, level_config)
        attempts += 1

        if attempts > level_config.max_attempts:
            print(f"Max attempts reached! You lost. Hidden number was {hidden_number}")
            break

        try:
            answer = get_answer(level_config)

            if answer == hidden_number:
                show_winning_info()
                break
            elif answer > hidden_number:
                print("Pick a smaller number")
            else:
                print("Pick a bigger number")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
