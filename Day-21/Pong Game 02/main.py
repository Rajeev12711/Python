from turtle import Screen, Turtle

screen =Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")


tim = Turtle()
tim.penup()
tim.goto(360, 0)
tim.color("white")
tim.shape("square")
tim.shapesize(stretch_wid=4,stretch_len=1)


def up():
    y_axis= tim.ycor()+20
    tim.goto(tim.xcor(), y_axis)

def down():
    y_axis=tim.ycor()-20
    tim.goto(tim.xcor(), y_axis)

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down, "Down")

screen.exitonclick()