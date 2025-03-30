from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen =Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


right= Paddle((371, 0))
left= Paddle((-371, 0))
ball = Ball()

screen.listen()
screen.onkey(right.up,"Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_on =True
while game_on:
    time.sleep(0.09)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor()>340 or ball.distance(left) < 50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor()>370 or ball.xcor() < -370:
        game_on =False

screen.exitonclick()