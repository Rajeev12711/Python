from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.point}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_point(self):
        self.clear()
        self.point += 1
        self.write(f"Score: {self.point}", align=ALIGN, font=FONT)

