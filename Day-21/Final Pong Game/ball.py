from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.movespeed = 0.1

    def move(self):
        x_point= self.xcor()+self.x_move
        y_point= self.ycor()+self.y_move
        self.goto(x_point, y_point)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.movespeed *= 0.9
        self.x_move *=-1

    def reset_ball(self):
        self.movespeed= 0.1
        self.goto(0,0)
        self.bounce_x()