import random

def choose_word():
    words = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Albus Dumbledore", "Severus Snape", "Lord Voldemort", "Tom Riddle", "Draco Malfoy", "Sirius Black", "Rubeus Hagrid", "Minerva McGonagall", "Remus Lupin", "Neville Longbottom", "Luna Lovegood", "Fred and George Weasley", "Ginny Weasley"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = len(word) + 3  # More attempts than the number of letters in the word
    
    print("Welcome to the Hangman game!")
    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ")
        
        if guess in guessed_letters:
            print("You have already guessed that letter. Please try a different one.")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("That letter is not in the word.")
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Remaining attempts: {attempts}")
        
        if attempts == 0:
            print(f"Sorry! You've run out of attempts. The correct word was {word}.")
            break

if __name__ == "__main__":
ط    play_hangman()
