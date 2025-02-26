from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
stock = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    choice = input(f"What would you like to have {item.get_items()}: ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        stock.report()
        money.report()
    else:
        drink = item.find_drink(choice)
        if stock.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                stock.make_coffee(drink)