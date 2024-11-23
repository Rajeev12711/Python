import os

print("Welcome to the secret auction bid.\nStart The bid Price")
bids =[]

def auction(name, price):
    bid = {
        "name":name,
        "price": float(price),     
    }
    bids.append(bid)

def highest(bids):
    higher =  0
    winner =""
    for bid in bids:
        if bid["price"] > higher:
            higher = bid["price"]
            winner = bid["name"]
    print(f"The winner is {winner} with a bid of ${higher:.2f}.")
 
again = True
while again:
    name = input("What is your Name? ")
    price = input("Enter your bid Price: ")
    auction(name, price)
    reuse= input("If there are other use than type 'yes' or not than 'no' ? \n")
    if reuse.lower() =="no":
        again=False
        highest(bids)
    elif reuse.lower() == "yes":
        os.system('cls')
        