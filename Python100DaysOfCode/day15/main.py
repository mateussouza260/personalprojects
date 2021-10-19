from drinksMenu import MENU, resources


def check_resources(drink):
    needed_supply = MENU[drink]["ingredients"]
    for item in needed_supply:
        if needed_supply[item] > resources[item]:
            print(f"Sorry, there is no {item}")
            return False
        else:
            return True


def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    print(f"Here is you {drink}, enjoy!")


def calc_money(drink):
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    money = (quarters + dimes + nickles + pennies)
    return money


def check_transaction(drink):
    if money < MENU[drink]["cost"]:
        print(f"Sorry that's not enough money. Money refunded:{money}.")
        return False
    else:
        change = money - MENU[drink]["cost"]
        print(f"Here is ${round(change, 2)} in change")
        return True


totalMoney = 0.0
is_on = True
while is_on:
    money = 0.00
    userChoice = input("What would you like> (espresso/latte/cappuccino): ").lower()
    if userChoice == "off":
        is_on = False
    elif userChoice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(totalMoney, 2)}")
    elif userChoice == "espresso":
        if check_resources("espresso"):
            money = calc_money("espresso")
            if check_transaction("espresso"):
                totalMoney += MENU["espresso"]["cost"]
                make_coffee("espresso")
    elif userChoice == "latte":
        if check_resources("latte"):
            money = calc_money("latte")
            if check_transaction("latte"):
                totalMoney += MENU["latte"]["cost"]
                make_coffee("latte")
    elif userChoice == "cappuccino":
        if check_resources("cappuccino"):
            money = calc_money("cappuccino")
            if check_transaction("cappuccino"):
                totalMoney += MENU["cappuccino"]["cost"]
                make_coffee("cappuccino")
