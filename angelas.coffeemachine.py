from reference import resources, MENU


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False



is_on = True
profit = 0
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml"),
        print(f"milk: {'milk'}ml"),
        print(f"coffee: {'coffee'}"),
        print(f"MOney: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"])

