from turtle import Turtle, Screen

app = Turtle()
screen = Screen()

def move_forward():
    app.forward(10)

def move_backward():
    app.backward(10)

def turn_left():
    app.left(10)

def turn_right():
    app.right(10)

def new_game():
    app.reset()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=new_game, key="c")

screen.exitonclick()