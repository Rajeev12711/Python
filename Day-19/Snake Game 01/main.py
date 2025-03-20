from turtle import Screen, Turtle
import time

screen =Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

index = [(0, 0),(-20,0), (-40,0)]

segment=[]

for i in index:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(i)
    segment.append(tim)

game_on =True
while game_on:
    screen.update()
    time.sleep(0.1)

    for z in range(len(segment)-1, 0, -1):
        new_x = segment[z-1].xcor()
        new_y = segment[z-1].ycor()
        segment[z].goto(new_x, new_y)
    segment[0].forward(20)

screen.exitonclick()