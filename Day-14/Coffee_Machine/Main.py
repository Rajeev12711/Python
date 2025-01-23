from idlelib.configdialog import changes

from Assets import MENU, resources


money = 0


def check_resources(user_choice):
    choice = MENU[user_choice]["ingredients"]
    for items in choice:
        if resources[items] < choice[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def process_coins():
    print("Insert a coins:")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many  dimes: ")) * 0.10
    nickles = int(input("How many  nickles: ")) * 0.05
    pennies = int(input("How many  pennies: ")) * 0.01
    total = quarters+ dimes+ nickles+ pennies
    return total


def check_transaction(payment_rec, price):
    price_check = MENU[price]["cost"]
    if payment_rec < price_check:
        print(f"Sorry that's not enough money ${payment_rec}. Money refunded.")
        return False
    else:
        change = round(payment_rec -price_check, 2)
        print(f"Here is ${change} dollars in change.")
        global money
        money += price_check
        return True


def deducted_resources(product):
    deducted = MENU[product]["ingredients"]
    for item in deducted:
        resources[item] -= deducted[item]
    print(f"Here is your {product}. Enjoy!.")


off_machine = True
while off_machine:
    user = input("What would you like to have (Espresso/Latte/Cappuccino): ").lower()
    if user == "off":
        off_machine = False
    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}" )
    elif user == "latte" or "espresso" or "cappuccino":
        if check_resources(user):
            payment = process_coins()
            if check_transaction(payment, user):
                deducted_resources(user)
