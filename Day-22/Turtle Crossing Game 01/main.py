from turtle import Turtle, Screen
from player import Player
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()


screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>280:
        player.reset_position()





screen.exitonclick()
