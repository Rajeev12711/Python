from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_side=0
        self.left_side=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.left_side} : {self.right_side} ", align=ALIGN, font=FONT)

    def l_side(self):
        self.left_side += 1
        self.update_score()

    def r_side(self):
        self.right_side+=1
        self.update_score()
