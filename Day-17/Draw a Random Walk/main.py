from turtle import Turtle, Screen
import random

app= Turtle()

colors = ["black", "white", "red", "green", "blue", "cyan", "yellow", "magenta",
    "gray", "brown", "orange", "purple", "pink", "gold", "silver", "maroon", "navy", "lime", "teal", "violet", "indigo"]
direction = [0, 90, 180, 270]

app.pensize(10)
app.speed("fast")

for i in range(0, 100):
    app.color(random.choice(colors))
    app.forward(100)
    app.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()

