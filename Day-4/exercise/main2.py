row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n {row2}\n {row3}")
position = input("where do you want to put the treasure? ")

row = int(position[0])-1
cloumn = int(position[1])-1

map[row][cloumn] ="X"




print(f"{row1}\n {row2}\n {row3}")