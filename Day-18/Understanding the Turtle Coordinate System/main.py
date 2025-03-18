from turtle import Turtle, Screen
import random

my_screen= Screen()
my_screen.setup(500, 400)
user = my_screen.textinput(title="Make a Guess", prompt="Which turtle will win the race? Enter a color:")
color= ["red", "blue", "orange", "green", "yellow", "purple"]
yaxis=[-70, -40, -10, 20, 50, 80]
arr_turtle=[]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230, y=yaxis[i])
    arr_turtle.append(tim)

race = True

while race:
    if user:
        for z in arr_turtle:
            if z.xcor()>230:
                winner= z.pencolor()
                race= False
                if user == z:
                    print(f"You've won! The {winner} turtle is winner!")
                else:
                    print(f"You've lost! The {winner} turtle is winner!")
            z.forward(random.randint(0, 10))
    else:
        race=False





my_screen.exitonclick()