from turtle import Screen
from paddle import Paddle

screen =Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

right= Paddle((350, 0))
left= Paddle((-350, 0))



screen.listen()
screen.onkey(right.up,"Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")


screen.exitonclick()