import random
name = input("give me everybody names , separated by cooma(,).\n")
name = name.split(",")

nameint=len(name)
person= random.randint(0, nameint-1)
pay =name[person]
print(pay)