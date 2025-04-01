from importlib.resources import contents
from turtle import Turtle

ALIGN="center"
FONT=("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.high_score = self.file_read()
        self.goto(0, 260)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.point} High Score: {self.high_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def file_read(self):
        with open("data.txt") as file:
            data = file.read()
        return int(data)

    def update_score(self):
        self.write(f"Score: {self.point} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_point(self):
        self.point += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        self.clear()
        if self.point>self.high_score:
            self.high_score=self.point
        self.point=0
        self.write(f"Score: {self.point} High Score: {self.high_score}", align=ALIGN, font=FONT)
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
