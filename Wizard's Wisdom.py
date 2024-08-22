# Define the list of questions and correct answers
questions = [
    {"question": "Is Harry Potter a boy?", "answer": "yes"},
    {"question": "Is Hermione Granger in Gryffindor house?", "answer": "yes"},
    {"question": "Was Severus Snape a Defense Against the Dark Arts teacher?", "answer": "no"},
    {"question": "Was Dumbledore the headmaster of Hogwarts?", "answer": "yes"},
    {"question": "Is Lord Voldemort's real name Tom Riddle?", "answer": "yes"},
    {"question": "Is Hagrid a giant?", "answer": "no"},
    {"question": "Is Hogwarts located in London?", "answer": "no"},
    {"question": "Does Harry Potter have red hair?", "answer": "no"},
    {"question": "Is Ron Weasley Harry's best friend?", "answer": "yes"},
    {"question": "Is Draco Malfoy in Slytherin house?", "answer": "yes"},
    {"question": "Is the Sorting Hat a magical object?", "answer": "yes"},
    {"question": "Did Harry Potter defeat Voldemort?", "answer": "yes"},
    {"question": "Is Professor McGonagall an Animagus?", "answer": "yes"},
    {"question": "Is the Quidditch pitch at Hogwarts?", "answer": "yes"},
    {"question": "Is Dobby a house-elf?", "answer": "yes"},
    {"question": "Is Lucius Malfoy a member of the Order of the Phoenix?", "answer": "no"},
    {"question": "Did Harry Potter live with the Dursleys?", "answer": "yes"},
    {"question": "Was the Triwizard Tournament held at Hogwarts?", "answer": "yes"},
    {"question": "Is Bellatrix Lestrange related to Sirius Black?", "answer": "yes"},
    {"question": "Is the Elder Wand one of the Deathly Hallows?", "answer": "yes"},
    {"question": "Is Neville Longbottom good at Potions?", "answer": "no"},
    {"question": "Is the Marauder's Map a magical map of Hogwarts?", "answer": "yes"},
    {"question": "Is Cedric Diggory from Hufflepuff house?", "answer": "yes"},
    {"question": "Is the Forbidden Forest forbidden to students?", "answer": "yes"},
    {"question": "Is Buckbeak a Hippogriff?", "answer": "yes"},
    {"question": "Did Harry Potter lose his parents to Voldemort?", "answer": "yes"},
    {"question": "Is Kreacher a house-elf loyal to Harry Potter?", "answer": "no"},
    {"question": "Is the Basilisk in the Chamber of Secrets a snake?", "answer": "yes"},
    {"question": "Is Professor Trelawney a teacher of Divination?", "answer": "yes"},
    {"question": "Is Fleur Delacour from Beauxbatons Academy?", "answer": "yes"}
]

# Initialize the score
score = 0

# Function to ask a question
def ask_question(question_data):
    global score
    answer = input(question_data["question"] + " (yes/no): ").strip().lower()
    if answer == question_data["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Main game loop
for i in range(5):
    print(f"Question {i+1}:")
    ask_question(questions[i])

# Final score and message
print(f"\nYour final score is {score} out of 5.")
if score == 5:
    print("Congratulations! You're a Harry Potter expert!")
elif score >= 3:
    print("Well done! You know quite a bit about Harry Potter.")
else:
    print("Better luck next time! Keep studying the magical world.")
