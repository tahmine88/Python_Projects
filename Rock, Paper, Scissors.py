import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list_play = ['Rock','Paper','Scissors']
list_play = random.choice(list_play)
player = input("choice beatween Rock,Paper,Scissors: ")

if player == 'Rock':
    if list_play == 'Rock':
        print('You: ',rock)
        print('Me: ',rock)
        result = "They are the same"
    elif list_play == 'Paper':
        print('You: ',rock)
        print('Me: ',paper)
        result = "I'm the winner"
    else:
        print('You: ',rock)
        print('Me: ',scissors)
        result = "You're the winner"


elif player == 'Paper':
    if list_play == 'Paper':
        print('You: ',paper)
        print('Me: ',paper)
        result = "They are the same"
    elif list_play == 'Scissors':
        print('You: ',paper)
        print('Me: ',scissors)
        result = "I'm the winner"
    else:
        print('You: ',paper)
        print('Me: ',rock)
        result = "You're the winner"


else:
    if list_play == 'Scissors':
        print('You: ',scissors)
        print('Me: ',scissors)
        result = "They are the same"
    elif list_play == 'Rock':
        print('You: ',scissors)
        print('Me: ',rock)
        result = "I'm the winner"
    else:
        print('You: ',scissors)
        print('Me: ',paper)
        result = "You're the winner"
print(result)

