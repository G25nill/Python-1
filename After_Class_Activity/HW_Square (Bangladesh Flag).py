import turtle

# screen
screen = turtle.Screen()
screen.bgcolor("white")

# turtle object
flag = turtle.Turtle()

# rectangle part of flag
flag.color("green")
flag.begin_fill()

for i in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(180)
    flag.right(90)

flag.end_fill()

# move to center for circle
flag.penup()
flag.goto(150, -120)
flag.pendown()

# red circle
flag.color("red")
flag.begin_fill()
flag.circle(50)
flag.end_fill()

turtle.done()