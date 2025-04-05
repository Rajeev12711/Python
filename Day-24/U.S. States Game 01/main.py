import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Guess The US States Name")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=740, height=520)

point = turtle.Turtle()

data  = pd.read_csv("50_states.csv")
all_state = data.state.to_list()


correct_answer=[]

game_on = True
while game_on:

    answer_state = screen.textinput(f"{len(correct_answer)} /{len(data)} States Correct", "Enter one State Name at  a time: ")
    answer_state = answer_state.title()
    if answer_state in all_state:
        correct_answer.append(answer_state)
        location= data[data.state == answer_state]
        point.hideturtle()
        point.penup()
        point.goto(int(location.x.iloc[0]), int(location.y.iloc[0]))
        point.write(f"{answer_state}", font=("Arial", 7, "normal"))



screen.exitonclick()