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
amount = 0


def print_report():
    """Print total of ingredients remaining and the profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def sum_coins(pennies, dimes, nickles, quarters):
    """Adds to coins that the customer has entered."""
    return round((pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25), 2)


def calculate_change(user_choice, amount):
    """Calculate customer change."""
    return round(amount - MENU[user_choice]['cost'], 2)


def check_resources(user_choice):
    """Check if machine has resources."""

    machine_resources = ''

    for i in MENU[user_choice]['ingredients']:
        ingredient = i
        amount = MENU[user_choice]['ingredients'][i]

        for i in resources:
            resources_ingredient = i
            resources_amount = resources[i]

            if ingredient == resources_ingredient:
                if amount > resources_amount:
                    machine_resources += ingredient
                else:
                    machine_resources += ''

    return machine_resources    


def update_resources(user_choice):
    """Update machine resources."""
    for i in MENU[user_choice]['ingredients']:
        ingredient = i
        ingredient_amount = MENU[user_choice]['ingredients'][i]

        for i in resources:
            resources_ingredient = i

            if ingredient == resources_ingredient:
                resources[i] -= ingredient_amount


def product_cost(user_choice):
    """Return cost to add to profit"""
    return MENU[user_choice]['cost']


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ")

    if user_choice == "report":
        print_report()
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        amount = sum_coins(quarters, dimes, nickles, pennies)

        change = calculate_change(user_choice, amount)
        machine_resources = check_resources(user_choice)

        if machine_resources == '':
            if change < 0:
                print("Insufficient balance.")
            else:
                update_resources(user_choice)
                profit += product_cost(user_choice)
                print(f"Here's {change} in change.")
                print(f"Here's is your {user_choice} ☕️. Enjoy!")
        else:
            print(f"Sorry there is not enough {machine_resources}.")
            





