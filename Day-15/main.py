from turtle import Turtle, Screen

box = Turtle()
print(box)
box.shape("triangle")
box.color("grey")
box.forward(100)
box.right(50)
box.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()


