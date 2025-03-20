import random

def guess_number_game():
    number_to_guess = random.randint(0, 10)
    attempts = 0
    while True:
        guess = int(input("Guess the number (0-10): "))
        attempts += 1
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

guess_number_game()