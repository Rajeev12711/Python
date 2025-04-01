from turtle import Screen
from snake import Snake
from food import  Food
from scoreboard import Score
import time

screen =Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on =True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<12:
        food.refresh()
        snake.extend_snake()
        score.increase_point()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset_snake()
        score.reset_score()

    for z in snake.segment[1:]:
        if snake.head.distance(z)<10:
            snake.reset_snake()
            score.reset_score()


screen.exitonclick()