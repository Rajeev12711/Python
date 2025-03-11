from turtle import Turtle, Screen

app = Turtle()

colors = ["gray", "brown", "orange", "purple", "pink", "gold", "silver", "maroon", "navy", "lime", "teal"]

def shape(num):
    angle = 360/ num
    for i in range(num):
        app.forward(100)
        app.right(angle)


for nums in range(3, 10):
    app.color(colors[nums])
    shape(nums)

screen =Screen()
screen.exitonclick()