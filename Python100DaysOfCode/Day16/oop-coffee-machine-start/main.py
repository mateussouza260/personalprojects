from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    available_drinks = Menu().get_items()
    user_choice = input(f"What drink are you having({available_drinks}): ").lower()
    if user_choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    elif user_choice == "off":
        is_on = False
    else:
        drink = Menu().find_drink(user_choice)
        print(drink.ingredients)
        if CoffeeMaker().is_resource_sufficient(drink):
            if MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)
