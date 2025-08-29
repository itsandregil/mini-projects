import random

from constants import MAX_ATTEMPTS


def get_answer() -> int:
    input_number = int(input("Pick a random number from 0 to 100: "))

    if input_number < 0 or input_number > 100:
        raise Exception("Number must be between 0 and 100")

    return input_number


def main():
    attempts = 0

    while True:
        attempts += 1
        hidden_number = random.randint(0, 100)

        if attempts > MAX_ATTEMPTS:
            print("Max attempts reached! You lost.")
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
