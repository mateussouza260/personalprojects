from drinksMenu import MENU, resources


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        return 1
    elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        return 3
    elif userChoice != "espresso":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            return 2
        else:
            return 0
    else:
        return 0


def subtract_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def check_money():
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    money = (quarters + dimes + nickles + pennies)
    return money


totalMoney = 0
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
        if resources_es == 0:
            money = check_money()
            if money < MENU["espresso"]["cost"]:
                print(f"Sorry that's not enough money. Money refunded:{money}.")
            else:
                change = money - MENU["espresso"]["cost"]
                print(f"Here is ${round(change, 2)} in change\nHere is you espresso, enjoy!")
                subtract_resources(userChoice)

                totalMoney += MENU["espresso"]["cost"]
        elif resources_es == 1:
            print("Sorry, water")
        elif resources_es == 2:
            print("Sorry, milk")
        elif resources_es == 3:
            print("Sorry, coffee")

    elif userChoice == "latte":
        resources_es = check_resources("latte")
        if resources_es == 0:
            money = check_money()
            if money < MENU["latte"]["cost"]:
                print(f"Sorry that's not enough money. Money refunded:{money}.")
            else:
                change = money - MENU["latte"]["cost"]
                print(f"Here is ${round(change, 2)} in change\nHere is you latte, enjoy!")
                subtract_resources(userChoice)

                totalMoney += MENU["latte"]["cost"]
        elif resources_es == 1:
            print("Sorry, water")
        elif resources_es == 2:
            print("Sorry, milk")
        elif resources_es == 3:
            print("Sorry, coffee")
    elif userChoice == "cappuccino":
        resources_es = check_resources("cappuccino")
        if resources_es == 0:
            money = check_money()
            if money < MENU["cappuccino"]["cost"]:
                print(f"Sorry that's not enough money. Money refunded:{money}.")
            else:
                change = money - MENU["cappuccino"]["cost"]
                print(f"Here is ${round(change, 2)} in change\nHere is you cappuccino, enjoy!")
                subtract_resources(userChoice)

                totalMoney += MENU["cappuccino"]["cost"]
        elif resources_es == 1:
            print("Sorry, water")
        elif resources_es == 2:
            print("Sorry, milk")
        else:
            print("Sorry, coffee")
