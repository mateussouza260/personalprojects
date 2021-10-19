from drinksMenu import MENU, resources


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        return "NoWater"
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        return "NoCoffee"
    elif userChoice != "espresso":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            return "NoMilk"
        else:
            return "AllGood"
    else:
        return "AllGood"


def resolve_resources(drink):
    if resources_es == "AllGood":
        calc_money(drink)
        return MENU[drink]["cost"]
    elif resources_es == "NoWater":
        print("Sorry, water")
        return 0
    elif resources_es == "NoMilk":
        print("Sorry, milk")
        return 0
    elif resources_es == "NoCoffee":
        print("Sorry, coffee")
        return 0


def subtract_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def calc_money(drink):
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    money = (quarters + dimes + nickles + pennies)
    if money < MENU[drink]["cost"]:
        print(f"Sorry that's not enough money. Money refunded:{money}.")
    else:
        change = money - MENU[drink]["cost"]
        print(f"Here is ${round(change, 2)} in change\nHere is you latte, enjoy!")
        subtract_resources(drink)


totalMoney = 0.0
is_on = True
while is_on:
    money = 0.00
    userChoice = input("What would you like> (espresso/latte/cappuccino): ").lower()
    if userChoice == "off":
        is_on = False
        break
    elif userChoice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n"
              f"Money: ${round(totalMoney, 2)}")
    elif userChoice == "espresso":
        resources_es = check_resources("espresso")
        totalMoney += resolve_resources(userChoice)
    elif userChoice == "latte":
        resources_es = check_resources("latte")
        totalMoney += resolve_resources(userChoice)
    elif userChoice == "cappuccino":
        resources_es = check_resources("cappuccino")
        totalMoney += resolve_resources(userChoice)
