from turtle import Screen
from player import Player
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
obstacle = Obstacle()


screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>280:
        player.reset_position()

    obstacle.create_obstacle()
    obstacle.move_obstacle()



screen.exitonclick()
