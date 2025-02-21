import random
name = input("Give me everybody names, separated by coma(,).\n")
name = name.split(",")

nameint=len(name)

person= random.randint(0, nameint-1)
pay =name[person]
print(pay)