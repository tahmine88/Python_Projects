#this project can be an online coing for you in a game:
# import random 
# rand = random.randint(0,1)
# if rand == 1:
#     print("Heads")
# else:
#     print('Tails')

#this project is about when you go out side like restaruant i can say wich person should pay for all:
# import random
# name_string = input("Give me everybody's names,seperated by a comma.")
# names = name_string.split(",")
# rand_int = random.randint(0,len(names)-1)x
# # buy_the_meal = names[rand_int]
# buy_the_meal = random.choice(names)
# print(buy_the_meal+" is going to buy the meal today ")

#this is like chess:
# row1 = ["1","2","3"]
# row2 = ["4","5","6"]
# row3 = ["7","8","9"]
# map = [row1,row2,row3]
# print(f'{row1}\n{row2}\n{row3}')
# number = str(int(input("please inter the number: ")))
# indexx = int(number[1]) - 1
# if number[0] == '1':
#     row1 = row1[indexx] = "x"
#     print(row1)
# elif number[0] == '2':
#     row2 = row2[indexx] = "x"
#     print(row2)
# else:
#     row3 = row3[indexx] = "x"
#     print(row3)

#this project is rock,paper, seciros:
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

