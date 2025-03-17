from turtle import Turtle, Screen

app = Turtle()
screen = Screen()

def move_forward():
    app.forward(100)

def move_right():
    app.right(90)
    app.forward(100)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Down", fun=move_right)

screen.exitonclick()