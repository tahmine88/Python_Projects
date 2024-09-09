import turtle
import random


screen = turtle.Screen()
screen.title("Turtle Trackers")
screen.bgcolor("white")


colors = ['pink', 'blue', 'orange', 'green', 'red', 'black', 'purple']
turtles = []


start_x = -200
start_y = -100
for color in colors:
    racer = turtle.Turtle(shape='turtle')
    racer.color(color)
    racer.penup()
    racer.goto(start_x, start_y)
    racer.pendown()
    turtles.append(racer)
    start_y += 50

user_guess = screen.textinput("Guess the Winner", "Which turtle will win the race? Enter a color: ")


winner = None
while True:
    for racer in turtles:
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= 200:
            winner = racer.color()[0]  
            break
    if winner:
        break


if user_guess == winner:
    print(f"Congratulations! The {winner} turtle won, and you guessed right!")
else:
    print(f"Sorry, the {winner} turtle won. You guessed {user_guess}, which was incorrect.")


screen.mainloop()
