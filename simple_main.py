from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True
cashMachine = MoneyMachine()
coffeeStatus = CoffeeMaker()
menu = Menu()
while machine_on:
    option = menu.get_items()
    cust_choice = input(f"What would you like? ({option}): \n").lower()
    if cust_choice == "off":
        machine_on = False
    elif cust_choice == "report":
        cashMachine.report()
        coffeeStatus.report()
    else:
        drink = menu.find_drink(cust_choice)
        if coffeeStatus.is_resource_sufficient(drink):
            if cashMachine.make_payment(drink.cost):
                coffeeStatus.make_coffee(drink)





