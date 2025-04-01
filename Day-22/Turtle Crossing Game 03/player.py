from turtle import Turtle

POSITION = (0, -280)
DISTANCE = 10

class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(POSITION)

    def move_up(self):
        self.forward(DISTANCE)

    def reset_position(self):
        self.goto(POSITION)
