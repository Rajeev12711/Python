def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiple(x, y):
    return x*y
def divide(x, y):
    return x/y
def module(x, y):
    return x%y

operations ={
    "+":add,
    "-":subtract,
    "*":multiple,
    "/":divide,
    "%": module
    }
x = float(input("enter the first number: "))
for operator in operations:
    print(operator)
symbol = input("Choose Any Operation From the Line Above: ")
y = float(input("enter the second number: "))
calculate = operations[symbol]
answer = calculate(x, y)

print(f"{x} {symbol} {y} = {answer}")
x = answer
for operator in operations:
    print(operator)
symbol = input("Choose Any Operation From the Line Above: ")
z = float(input("enter the third number: "))
calculate = operations[symbol]
answer = calculate(x, z)
print(f"{x} {symbol} {z} = {answer}")