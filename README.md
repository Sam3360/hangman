# Hangman Game

A classic word-guessing game implemented in Python, played directly in your console. Guess the hidden word letter by letter before the hangman figure is complete!

## Features

* **Diverse Word List:** Words are chosen from a broad general knowledge vocabulary, ensuring a varied and engaging experience.
* **Player vs. Computer:** The game randomly selects a word for you to guess.
* **ASCII Art Hangman:** Visual feedback on your remaining attempts with an evolving hangman figure.
* **Console-Based:** Play conveniently in your terminal or command prompt.
* **Continuous Play:** Option to play multiple rounds until you decide to quit.
* **Input Validation:** Ensures you enter valid single-letter guesses.
* **Tracked Guesses:** Keeps a record of incorrect letters you've already tried.

## How It Works

The game logic is straightforward:
1.  A word is randomly selected from a predefined list.
2.  The word is displayed as a series of underscores (`_`).
3.  You guess letters one at a time.
4.  If the letter is in the word, it's revealed in its correct position(s).
5.  If the letter is not in the word, a part of the hangman figure is drawn, and you lose a life.
6.  You win if you guess all letters before the hangman figure is fully drawn.
7.  You lose if the hangman figure is completed before you guess the word.

The `random` module is used for word selection. The hangman stages are represented by ASCII art strings.

## Requirements

* Python 3.x (No external libraries required)

## How to Run the Application

1.  **Save the Code:**
    * Copy the entire Python code for the Hangman game (the version with the diverse `WORDS` list) into a file named `hangman_game.py` (or any other name ending with `.py`).
2.  **Open Your Terminal/Command Prompt:**
    * Navigate to the directory where you saved `hangman_game.py`.
        * Example (Windows): `cd C:\Users\YourUser\Documents\my_games`
        * Example (macOS/Linux): `cd ~/Documents/my_games`
3.  **Run the Script:**
    * Execute the Python script using the command:
        ```bash
        python hangman_game.py
        ```

## How to Play

1.  When you run the script, you'll see a welcome message.
2.  The hidden word will be displayed as underscores, along with the hangman figure.
3.  You will be prompted to "Guess a letter:".
4.  Type a single letter (case-insensitive) and press Enter.
5.  The game will update the word display and the hangman figure based on your guess.
6.  You'll see your incorrect guesses listed and your remaining lives.
7.  After each round, you'll be asked if you want to play again. Type `yes` to play another round, or `no` to quit.

## Possible Enhancements

* **Difficulty Levels:** Categorize words by length or complexity into Easy, Medium, and Hard levels.
* **Hints:** Implement a hint system (e.g., reveal a letter at the cost of a life).
* **GUI:** Develop a graphical user interface using libraries like Tkinter, PyQt, or Kivy.
* **Score Tracking:** Keep track of wins and losses across multiple game sessions (requires file I/O for persistence).
* **Themed Word Lists:** Allow the user to choose a specific category (e.g., "Animals," "Countries," "Food").
* **Word Input:** Allow a second player to input a word for the first player to guess.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
