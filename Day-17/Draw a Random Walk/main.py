from turtle import Turtle, Screen
import random
import colorsys

app= Turtle()

colors = [
    "Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black",
    "Cyan", "Magenta", "Lime", "Olive", "Teal", "Maroon", "Navy", "Gray", "Silver", "Gold",
    "Beige", "Turquoise", "Violet", "Indigo", "Coral", "Lavender", "Salmon", "Crimson", "Azure", "Mint" ]
direction = [0, 90, 180, 270]

app.pensize(10)
app.speed("fast")

for i in range(0, 100):
    app.color(random.choice(colors))
    app.forward(100)
    app.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()

