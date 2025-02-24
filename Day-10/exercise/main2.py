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
    print("Welcome to world of Calculation.")
    x = float(input("Enter the First Number: "))
    again = True
    while again == True:
        for operator in operations:
            print(operator)
        symbol = input("Choose any operation from the line above: ")
        y = float(input("Enter the next number: "))
        calculate = operations[symbol]
        answer = calculate(x, y)

        print(f"{x} {symbol} {y} = {answer}")
        x = answer
        
        reuse = input(f"Enter 'Yes' to continue calculating with {answer}, or enter 'No' to Start new calculation, or Enter 'Exit' for Exit the calculater: ")
        if reuse.lower()  == "no":
            again = False
            calculater()
        elif reuse.lower() == "yes":
            again = True
        elif reuse.lower() == "exit":
            again =False
        else:
            again = False
            print("Invaild")

calculater() 
