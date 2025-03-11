from turtle import Turtle, Screen

app = Turtle()

colors = ["Cyan", "Magenta", "Lime", "Olive", "Teal", "Maroon", "Navy", "Gray", "Silver", "Gold"]

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