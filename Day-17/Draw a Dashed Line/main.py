from turtle import Turtle, Screen

dashed = Turtle()

for _ in range(16):
    dashed.forward(10)
    dashed.penup()
    dashed.forward(10)
    dashed.pendown()


screen = Screen()
screen.exitonclick()