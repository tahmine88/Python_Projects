import turtle


window = turtle.Screen()
window.title("Path Painter")
window.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)
pen.shape("turtle")

def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def turn_left():
    pen.left(45)


def turn_right():
    pen.right(45)


window.listen()
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")


window.mainloop()
