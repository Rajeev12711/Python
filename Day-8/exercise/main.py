import math
def paint(height, width, coverage):
   box = ((height * width) / coverage)
   boxes = math.ceil(box)
   print(f"You'll need {boxes} boxes")

height =  int(input("Enter the height(meter) of wall = "))
width = int(input("Enter the width(meter) of wall = "))
coverage = 5
paint(height, width, coverage)