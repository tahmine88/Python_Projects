import tkinter as tk
import random
import time

# Extended dictionary of English-French word pairs (some correct, some incorrect)
word_pairs = [
    ("apple", "pomme"),  # correct
    ("car", "voiture"),  # correct
    ("dog", "chien"),    # correct
    ("house", "maison"), # correct
    ("red", "rouge"),    # correct
    ("blue", "bleu"),    # correct
    ("table", "table"),  # correct
    ("book", "livre"),   # correct
    ("water", "eau"),    # correct
    ("food", "nourriture"),  # correct
    ("sun", "soleil"),   # correct
    ("moon", "lune"),    # correct
    ("cat", "chat"),     # correct
    ("tree", "arbre"),   # correct
    ("milk", "lait"),    # correct
    ("bread", "pain"),   # correct
    ("city", "ville"),   # correct
    ("teacher", "professeur"),  # correct
    ("student", "étudiant"),  # correct
    ("pen", "stylo"),    # correct
    ("plane", "avion"),  # correct
    ("music", "musique"),  # correct
    ("chair", "chaise"),  # correct
    ("dog", "chat"),     # incorrect
    ("book", "chaise"),  # incorrect
    ("blue", "rouge"),   # incorrect
    ("car", "chien"),    # incorrect
    ("milk", "eau"),     # incorrect
    ("city", "table")    # incorrect
]

class FlashcardGame:
    def __init__(self, master):
        self.master = master
        self.master.title("LanguaMatch - English-French Flashcard Game")
        self.master.geometry("400x300")
        self.master.config(bg="#f7f7f7")

        self.score = 0
        self.current_stage = 0
        self.max_stages = 10

        # Add a colorful header
        self.label = tk.Label(master, text="Get ready!", font=("Helvetica", 18, "bold"), bg="#ffcccb", fg="black")
        self.label.pack(pady=20, fill=tk.X)

        # Display flashcard with padding and background
        self.word_label = tk.Label(master, text="", font=("Helvetica", 24), bg="white", fg="black", width=15, height=2, relief="solid")
        self.word_label.pack(pady=20)

        # Buttons with stylish colors
        self.correct_button = tk.Button(master, text="Correct", command=self.correct_choice, font=("Helvetica", 14), bg="#8bc34a", fg="white", activebackground="#4caf50", state="disabled")
        self.correct_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.incorrect_button = tk.Button(master, text="Incorrect", command=self.incorrect_choice, font=("Helvetica", 14), bg="#f44336", fg="white", activebackground="#e57373", state="disabled")
        self.incorrect_button.pack(side=tk.RIGHT, padx=20, pady=20)

        self.next_flashcard()

    def next_flashcard(self):
        if self.current_stage == self.max_stages:
            self.end_game("You know French well! Congratulations!")
            return

        # Pick a random pair of words
        self.english_word, self.french_word = random.choice(word_pairs)
        self.word_label.config(text=self.english_word)

        # Disable buttons before showing French word
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")
        
        # After 5 seconds, show the French word and enable buttons
        self.master.after(5000, self.show_french_word)

    def show_french_word(self):
        self.word_label.config(text=self.french_word)
        self.correct_button.config(state="normal")
        self.incorrect_button.config(state="normal")

    def correct_choice(self):
        if (self.english_word, self.french_word) in word_pairs[:20]:
            self.current_stage += 1
            self.score += 1
            self.label.config(text="Correct!", bg="#8bc34a", fg="white")
            self.next_flashcard()
        else:
            self.end_game(f"You lost! Your score is {self.score}")

    def incorrect_choice(self):
        if (self.english_word, self.french_word) not in word_pairs[:20]:
            self.current_stage += 1
            self.score += 1
            self.label.config(text="Correct!", bg="#8bc34a", fg="white")
            self.next_flashcard()
        else:
            self.end_game(f"You lost! Your score is {self.score}")

    def end_game(self, message):
        self.label.config(text=message, bg="#f44336", fg="white")
        self.word_label.config(text="")
        self.correct_button.config(state="disabled")
        self.incorrect_button.config(state="disabled")
        self.master.after(3000, self.master.quit)

# Run the game
root = tk.Tk()
game = FlashcardGame(root)
root.mainloop()
