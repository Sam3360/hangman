import random


HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
      /    |
           |
           |
        -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
        -------
    """
]

WORDS = [
    "APPLE", "BANANA", "ELEPHANT", "GUITAR", "OCEAN",
    "MOUNTAIN", "LIBRARY", "SUNFLOWER", "RAINBOW", "BUTTERFLY",
    "PYRAMID", "VIOLIN", "ASTRONOMY", "CHOCOLATE", "ADVENTURE",
    "BLOSSOM", "CRICKET", "DIAMOND", "FANTASY", "GLOBE",
    "HARMONY", "IGLOO", "JUNGLE", "KANGAROO", "LANTERN",
    "MAGNIFY", "NOODLE", "ORANGE", "PENGUIN", "QUICK",
    "ROBOT", "SPARROW", "TREASURE", "UMBRELLA", "VOLCANO",
    "WATERMELON", "XYLOPHONE", "YACHT", "ZEBRA", "COFFEE",
    "EXPLORE", "FROZEN", "MARBLE", "NEWSPAPER", "WHISPER"
]


def get_random_word(word_list):
    """Selects a random word from the given list."""
    return random.choice(word_list) 

def display_game_state(word, guessed_letters, incorrect_guesses_count, incorrect_guesses_list):
    """Displays the current state of the word, guessed letters, and hangman stage."""
    print(HANGMAN_STAGES[incorrect_guesses_count])

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"\nWord: {display_word.strip()}")

    
    print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses_list))}")
    
    
    lives_left = len(HANGMAN_STAGES) - 1 - incorrect_guesses_count
    print(f"Lives left: {lives_left}")

def play_hangman():
    """Main function to play a single round of Hangman."""
    word_to_guess = get_random_word(WORDS)
    guessed_letters = set() 
    incorrect_guesses_count = 0 
    incorrect_guesses_list = [] 
    max_incorrect_guesses = len(HANGMAN_STAGES) - 1 

    print("--- Welcome to Hangman! ---")
    print("Guess the word, one letter at a time.")

    while incorrect_guesses_count < max_incorrect_guesses:
        display_game_state(word_to_guess, guessed_letters, incorrect_guesses_count, incorrect_guesses_list)

        
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            print("You win!")
            return True 

        guess = input("Guess a letter: ").upper().strip() 

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess) 

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses_count += 1
            incorrect_guesses_list.append(guess) 

  
    display_game_state(word_to_guess, guessed_letters, incorrect_guesses_count, incorrect_guesses_list) 
    print("\nGame Over!")
    print(f"The word was: {word_to_guess}")
    print("You ran out of guesses.")
    return False 

def main():
    """Manages playing multiple rounds of Hangman."""
    while True:
        play_hangman()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()
