from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        x_point= self.xcor()+10
        y_point= self.ycor()+10
        self.goto(x_point, y_point)