import turtle
import time
import random

delay = 0.15  


score = 0
high_score = 0


wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  


head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")


while True:
    wn.update()


    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        print(f"Game Over! You ate {score // 10} apples.")  
        time.sleep(1)
        break  


    if head.distance(food) < 20:

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            print(f"Game Over! You ate {score // 10} apples.")  
            time.sleep(1)
            break  

    time.sleep(delay)


wn.bye()
