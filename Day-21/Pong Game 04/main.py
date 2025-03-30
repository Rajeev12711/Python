from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen =Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


right= Paddle((350, 0))
left= Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right.up,"Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_on =True
while game_on:
    time.sleep(0.06)
    screen.update()
    ball.move()


screen.exitonclick()