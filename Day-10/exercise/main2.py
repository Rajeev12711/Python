def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiple(x, y):
    return x*y
def divide(x, y):
    if y == 0:
        return
    return x / y
def module(x, y):
    return x%y

operations ={
    "+":add,
    "-":subtract,
    "*":multiple,
    "/":divide,
    "%": module
    }

def  calculater():
    print("Welcome to world of Calculation")
    x = float(input("enter the first number: "))
    again = True
    while again == True:
        for operator in operations:
            print(operator)
        symbol = input("Choose Any Operation From the Line Above: ")
        y = float(input("enter the next number: "))
        calculate = operations[symbol]
        answer = calculate(x, y)

        print(f"{x} {symbol} {y} = {answer}")
        x = answer
        
        reuse = input(f"Type 'yes' to continue calculating with  {answer}, or type 'no' to Start new calculation, or type 'Exit' for Exit the calculater: ")
        if reuse.lower()  == "no":
            again = False
            calculater()
        elif reuse.lower() == "yes":
            again = True
        elif reuse.lower() == "exit":
            again =False
        else:
            again = False
            print("Invaild ")

calculater() 
