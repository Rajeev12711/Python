from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "green", "purple", "yellow"]
START_DISTANCE = 5
INCREASE_TIME = 5

class Obstacle:
    
    def __init__(self):
        self.obstacle_speed = START_DISTANCE
        self.all_obstacle = []

    def create_obstacle(self):
        create_random = random.randint(1,6)
        if create_random ==1:
            new_obstacle = Turtle("square")
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            new_obstacle.penup()
            new_obstacle.color(random.choice(COLORS))
            y_axis = random.randint(-250, 250)
            new_obstacle.goto(300, y_axis)
            self.all_obstacle.append(new_obstacle)

    def move_obstacle(self):
        for obstacle_move in self.all_obstacle:
            obstacle_move.backward(self.obstacle_speed)

    def leve_up(self):
        self.obstacle_speed += INCREASE_TIME
