import random
import turtle as t
from turtle import Screen

app =t.Turtle()

t.colormode(255)

app.speed("fastest")

size_of_gap=10

def colors():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color=(r, g, b)
    return color


app.speed("fastest")
for i in range(int(360/size_of_gap)):
    app.color(colors())
    app.circle(100)
    app.setheading(app.heading()+size_of_gap)

screen=Screen()
screen.exitonclick()
