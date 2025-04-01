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
        obstacle.leve_up()

    obstacle.create_obstacle()
    obstacle.move_obstacle()

    for obstacle_one in obstacle.all_obstacle:
        if obstacle_one.distance(player)<20:
            game_on= False



screen.exitonclick()
