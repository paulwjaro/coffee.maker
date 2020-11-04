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

prompts = ["espresso", "latte", "cappuccino", "report", "off"]


def run_coffee_maker():
    selection = input("What would you like? (espresso, latte, cappuccino):")
    if selection.lower() == prompts[0]:
        print(prompts[0])
        run_coffee_maker()
    elif selection.lower() == prompts[1]:
        print(prompts[1])
        run_coffee_maker()
    elif selection.lower() == prompts[2]:
        print(prompts[2])
        run_coffee_maker()
    elif selection.lower() == prompts[3]:
        print(prompts[3])
        run_coffee_maker()
    elif selection.lower() == prompts[4]:
        print("Machine Off.")
    else:
        print("Not a valid Selection")
        run_coffee_maker()


run_coffee_maker()

# TODO: 1. Create Report of Available Resources

# TODO: 1.1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 1.1.a Check the user’s input to decide what to do next.
# TODO: 1.1.b The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt
#  should show again to serve the next customer.

# TODO: 1.2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 1.2.a For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#   the machine. Your code should end execution when this happens.

# TODO: 1.3. Print report.
# TODO: 1.3.a  When the user enters “report” to the prompt, a report should be generated that shows
#   the current resource values. e.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5


