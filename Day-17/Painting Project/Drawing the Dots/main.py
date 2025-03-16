import random
import turtle

turtle.colormode(255)
app = turtle.Turtle()

color_list= [[201, 161, 98], [32, 175, 114], [137, 91, 52], [219, 216, 90], [66, 173, 223], [159, 4, 90], [8, 113, 187], [157, 159, 60], [232, 41, 125], [241, 87, 36], [213, 222, 21], [104, 195, 140], [27, 165, 212], [204, 32, 110], [218, 129, 172], [3, 158, 144], [147, 216, 190], [236, 164, 199], [100, 62, 22], [144, 210, 227], [242, 170, 148], [92, 55, 20], [50, 138, 208], [151, 198, 234], [127, 0, 67], [255, 2, 108]]

app.speed("fastest")
app.penup()
app.hideturtle()
app.setheading(230)
app.forward(300)
app.setheading(0)

num_dots=101

for i in range(1, num_dots):
    app.dot(20, random.choice(color_list))
    app.forward(50)
    if i % 10 ==0:
        app.setheading(90)
        app.forward(50)
        app.setheading(180)
        app.forward(500)
        app.setheading(0)


screen = turtle.Screen()
screen.exitonclick()