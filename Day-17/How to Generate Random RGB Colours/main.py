import turtle as t
import random


app= t.Turtle()

t.colormode(255)

def colours():
    r =random.randint(0, 255)
    g =random.randint(0, 255)
    b =random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

app.pensize(10)
app.speed("fast")

for i in range(0, 100):
    app.color(colours())
    app.forward(100)
    app.setheading(random.choice(direction))


