from reference import resources, MENU

# TODO 1. print report


def report(resource):
    for key in resource:
        unit = "ml"
        if key == "coffee":
            unit = "g"
        elif key == "money":
            unit = "$"
        print(f"{key}: {resource[key]}{unit}")


# TODO 2.2  CHECK RESOURCES IF SUFFICIENT?


def check_resource():
    if water >= choice_water and milk >= choice_milk and coffee >= choice_coffee:
        return True
    else:
        return False

# TODO 3. PROCESS COINS


def coin_counter():
    c_money = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    return c_money


# TODO 4. CHECK TRANSACTION SUCCESSFUL?


def transaction(coins, cost):
    change = round(coins - cost, 2)
    if coins > cost:
        return f"Here is ${change} in change.\nHere is your {choice}. Enjoy!"
    else:
        return "Sorry that 's not enough money. Money refunded."

# TODO 5. MAKE COFFEE.


make_coffee = True
while make_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice == "report":
        if choice == "report":
            report(resources)
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        make_coffee = False
    else:
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        choice_milk = 0
        if choice == "espresso":
            choice_milk == 0
        else:
            choice_milk = MENU[choice]["ingredients"]["milk"]
        choice_water = MENU[choice]["ingredients"]["water"]
        choice_coffee = MENU[choice]["ingredients"]["coffee"]
        choice_cost = MENU[choice]["cost"]

        if not check_resource():
            print("Sorry not enough water")
        else:
            quarters = int(input("Please insert coins.\nhow many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            resources["water"] -= choice_water
            resources["milk"] -= choice_milk
            resources["coffee"] -= choice_coffee
            print(transaction(coin_counter(), choice_cost))