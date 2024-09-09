import turtle
import random
import time

# Set up the screen
win = turtle.Screen()
win.title("Turtle Escape")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)

# Level and speed
level = 1
speed = 1.5
time_per_level = 15  # Time to complete each level in seconds

# Draw the level on the screen
level_display = turtle.Turtle()
level_display.speed(0)
level_display.color("black")
level_display.penup()
level_display.hideturtle()
level_display.goto(-350, 260)
level_display.write(f"Level: {level}", align="left", font=("Courier", 24, "normal"))

# Create the player (turtle)
player = turtle.Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.goto(-300, 0)

# Create the cars (obstacles)
colors = ["red", "blue", "yellow", "green", "purple", "orange"]
cars = []

def create_cars(num):
    for _ in range(num):
        car = turtle.Turtle()
        car.shape("square")
        car.color(random.choice(colors))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(400, random.randint(-250, 250))
        cars.append(car)

# Control player movement
def move_up():
    y = player.ycor()
    if y < 250:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -250:
        player.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")

# Function to check for collision
def check_collision():
    for car in cars:
        if player.distance(car) < 20:
            return True
    return False

# Function to move cars
def move_cars():
    for car in cars:
        car.setx(car.xcor() - random.uniform(2.0, 4.5) * speed)  # Increased speed variation
        if car.xcor() < -400:
            car.goto(400, random.randint(-250, 250))

# Update the level and display level completion message
def update_level():
    global level, speed
    level += 1
    speed += 0.5
    level_display.clear()
    level_display.write(f"Level: {level}", align="left", font=("Courier", 24, "normal"))
    # Display level completion message
    level_complete = turtle.Turtle()
    level_complete.speed(0)
    level_complete.color("blue")
    level_complete.penup()
    level_complete.hideturtle()
    level_complete.goto(0, 0)
    level_complete.write(f"Level {level - 1} Complete!", align="center", font=("Courier", 36, "bold"))
    time.sleep(2)  # Show the message for 2 seconds
    level_complete.clear()

# Main game loop
def game_loop():
    global level
    create_cars(15)
    
    start_time = time.time()  # Track the start time for each level
    
    while level <= 5:
        win.update()
        move_cars()

        if check_collision():
            time.sleep(1)
            print("Game Over! You Lost.")
            win.bye()  # Close the window
            break

        time.sleep(0.03)

        # Check if the player has completed the current level based on time
        if time.time() - start_time >= time_per_level:
            update_level()
            start_time = time.time()  # Reset the timer for the next level

        # If the player wins all 5 levels
        if level == 6:  # If player has completed level 5 and reaches level 6
            level_display.clear()
            level_display.write("Congratulations! You Won!", align="center", font=("Courier", 36, "bold"))
            time.sleep(3)
            win.bye()  # Close the window
            break

game_loop()
