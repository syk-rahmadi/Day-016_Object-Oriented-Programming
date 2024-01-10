from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




#TODO 2. Turn off the Coffe Machine by entering "off"
machine_on = True

#TODO 3. Print report
cashMachine = MoneyMachine()
coffeeStatus = CoffeeMaker()

#TODO 4. Check resources sufficient
menu = Menu()

while machine_on:
    option = menu.get_items()
    # TODO 1. Prompt user by asking their choice
    cust_choice = input(f"What would you like? ({option}): \n").lower()
    if cust_choice == "off":
        machine_on = False
    elif cust_choice == "report":
        cashMachine.report()
        coffeeStatus.report()
    else:
        drink = menu.find_drink(cust_choice)
        if coffeeStatus.is_resource_sufficient(drink):
        # TODO 5. Process coins
        # TODO 6. Check transaction successful
            if cashMachine.make_payment(drink.cost):
                # TODO 7. Make coffee
                coffeeStatus.make_coffee(drink)





