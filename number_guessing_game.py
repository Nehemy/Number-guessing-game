from art import logo
import random

number = random.choice(range(1, 101))
attempts = 0
guessed_number = 0

def guess():
    global guessed_number
    guessed_number = int(input("Make a guess: "))

def play_game():
    global number
    global attempts
    print(logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        attempts += 5
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess()
    else:
        attempts += 10
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess()

    game_on = True

    while guessed_number != number:

        if guessed_number == number:
            print(f"You got it! The answer was {number}.")
            return

        elif guessed_number > number:
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                return
            else:
                print(f"Too high \nGuess again. \nYou have {attempts} attempts remaining to guess the number.")
            guess()

        elif guessed_number < number:
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                return
            else:
                print(f"Too low \nGuess again. \nYou have {attempts} attempts remaining to guess the number.")
                guess()

play_game()