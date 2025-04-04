from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250 )
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)