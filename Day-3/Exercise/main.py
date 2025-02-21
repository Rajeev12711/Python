print("Welcome to Python Pizza Deliveries!") 
size = input("What size pizza do you want? S, M, or L: ").lower()
bill = 0
if size=="s":
    bill=15
    add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
    if add_pepperoni=="y":
        bill+=2
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese=="y":
        bill+=1
elif size=="m":
    bill=20
    add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
    if add_pepperoni=="y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese=="y":
        bill+=1
elif size=="l":
    bill=25
    add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
    if add_pepperoni=="y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese=="y":
        bill+=1
else:
    print("please choice right symbol")

print("Your bill is" ,bill)
    