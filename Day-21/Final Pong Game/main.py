from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen =Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right= Paddle((380, 0))
left= Paddle((-380, 0))

ball = Ball()
score= Score()

screen.listen()
screen.onkey(right.up,"Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_on =True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor()>350 or ball.distance(left) < 50 and ball.xcor()<-350:
        ball.bounce_x()

    if ball.xcor()>360:
        ball.reset_ball()
        score.l_side()

    if ball.xcor() < -360:
        ball.reset_ball()
        score.r_side()

screen.exitonclick()