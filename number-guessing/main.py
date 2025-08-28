import random

MAX_ATTEMPTS = 10


def main():
    attempts = 0
    random_number = random.randint(0, 100)

    while attempts < MAX_ATTEMPTS:
        attempts += 1
        user_number = int(input("Pick a random number from 0 to 100: "))

        if user_number < 0 or user_number > 100:
            print("Number should be between 0 and 100!")

        if user_number == random_number:
            print("You guessed it! You won.")
            break
        elif user_number > random_number:
            print("Pick a smaller number")
        elif user_number < random_number:
            print("Pick a bigger number")

    if attempts > MAX_ATTEMPTS:
        print("Max attempts reached! You lost.")


if __name__ == "__main__":
    main()
