#this project is hangman:
import random

def choose_word(word_list):
    return random.choice(word_list)

def hangman():
    words = ["python", "hangman", "challenge", "programming", "computer", "science", "mathematics", "game", "puzzle", "education"]
    secret_word = choose_word(words)
    guessed = "_" * len(secret_word)
    guessed_correctly = set()
    tries = 6

    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    print("Let's play Hangman!")
    print(stages[len(stages) - 1 - tries])
    print("Word to guess:", guessed)

    while tries > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_correctly:
                print("You already guessed that letter.")
            elif guess in secret_word:
                guessed_correctly.add(guess)
                guessed = "".join([letter if letter in guessed_correctly else "_" for letter in secret_word])
                print("Good guess:", guessed)
            else:
                guessed_correctly.add(guess)
                tries -= 1
                print(f"Wrong guess. {tries} tries left.")
                print(stages[len(stages) - 1 - tries])
        else:
            print("Invalid input. Please enter a single alphabetical character.")

    if "_" not in guessed:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("Game over. The word was:", secret_word)
        print(stages[0])

# Run the game
hangman()

