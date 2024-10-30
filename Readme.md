# Number Guessing Game

Welcome to the **Number Guessing Game**! This Python game challenges you to guess a randomly selected number between 1 and 100. You can choose between two difficulty levels and receive feedback on each guess until you either find the correct number or run out of attempts.

## Features
- **Difficulty Levels**:
  - **Easy Mode**: 10 attempts to guess the number.
  - **Hard Mode**: 5 attempts to guess the number.
- **Guess Feedback**: After each guess, you receive feedback indicating whether your guess was "Too high" or "Too low."
- **Game Outcome**: Win by guessing the correct number within the allowed attempts, or lose if you run out of guesses.

## How to Play
1. **Start the Game**: Run the script, and the game will welcome you with a logo and prompt you to select a difficulty level.
2. **Make Guesses**: Enter your guesses as prompted. Each guess will adjust your remaining attempts based on the game's feedback.
3. **Win or Lose**: You win by guessing the number correctly within the allowed attempts, or you lose if your attempts reach zero.

## Code Structure
- **guess()**: Prompts the player to enter a guess and checks it against the target number.
- **Game Logic**:
  - Sets difficulty level.
  - Provides feedback and tracks the number of attempts based on difficulty.

## Requirements
- Python 3.x
- `art.py` file: Included in the repository to display the game logo.

## How to Run
1. Clone or download this repository.
2. Open a terminal in the directory containing the files.
3. Run the game:
   ```bash
   python number_guessing_game.py

