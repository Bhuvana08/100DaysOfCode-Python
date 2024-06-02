MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def print_report(resources):
    """Prints the report of the resources"""
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${profit}")


def check_resources_sufficient(coffee_type):
    """Returns True if resources are sufficient else returns false"""
    resources_needed = MENU[coffee_type]["ingredients"]
    for item in resources_needed:
        if resources_needed[item] > resources[item] :
            print(f"There is no enough {item}")
            return False
    return True


def process_coins():
    """Process the coins and returns total"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(coffee_type):
    """Makes the coffee and deduct the resources"""
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    for element in coffee_ingredients:
        resources[element] -= coffee_ingredients[element]
    print(f"Here is your {coffee_type} ☕. Enjoy!")


is_on = True
while is_on:
    user_prompt = input("What would you like ? (espresso/latte/cappuccino) : ")
    if user_prompt == "report":
        print_report(resources)
    elif user_prompt == "off":
        # print("Coffe machine went off condition")
        is_on = False
    else:
        is_resources_sufficient = check_resources_sufficient(user_prompt)
        if is_resources_sufficient:
            amount = process_coins()
            if amount >= MENU[user_prompt]["cost"]:
                profit += MENU[user_prompt]["cost"]
                change = amount - MENU[user_prompt]["cost"]
                print(f"Here is ${change:.2f} in change")
                make_coffee(user_prompt)
            else:
                print("Not enough money. Money refunded!")


