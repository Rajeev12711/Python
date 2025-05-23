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

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on = False
        score.game_over()

    for z in snake.segment:
        if snake.head == z:
            pass
        elif snake.head.distance(z)<10:
            game_on =False
            score.game_over()


screen.exitonclick()