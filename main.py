MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

payment = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01,
}

prompts = ["espresso", "latte", "cappuccino", "report", "off"]


def run_coffee_maker():
    selection = input("What would you like? (espresso, latte, cappuccino):").lower()
    if selection == prompts[0] or selection.lower() == prompts[1] or selection.lower() == prompts[2]:
        print("You have selected: " + selection.capitalize())
        if resources["water"] >= MENU[selection]["ingredients"]["water"]:
            if resources["milk"] >= MENU[selection]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU[selection]["ingredients"]["coffee"]:
                    calculate_payment(MENU[selection]["cost"], MENU[selection]["ingredients"]["water"],
                                      MENU[selection]["ingredients"]["milk"], MENU[selection]["ingredients"]["coffee"])
                else:
                    print("Sorry, this machine is out of required coffee. Please try again later.")
            else:
                print("Sorry, this machine is out of required milk. Please try again later.")
        else:
            print("Sorry, this machine is out of required water. Please try again later.")
        run_coffee_maker()
    elif selection == prompts[3]:
        print("Machine Resource Report")
        print("Water: " + str(resources["water"]))
        print("Milk: " + str(resources["milk"]))
        print("Coffee: " + str(resources["coffee"]))
        print("Money: $" + str(resources["money"]))
        run_coffee_maker()
    elif selection == prompts[4]:
        print("Machine Off.")
    else:
        print("Not a valid Selection")
        run_coffee_maker()


def take_money():
    coin_taken = input("Please Insert Coin or Request Refund:").lower()

    if coin_taken == "refund":
        return -1

    if coin_taken == "quarter":
        how_many = input("How Many?: ")
        return payment[coin_taken] * float(how_many)
    elif coin_taken == "dime":
        how_many = input("How Many?: ")
        return payment[coin_taken] * float(how_many)
    elif coin_taken == "nickle":
        how_many = input("How Many?: ")
        return payment[coin_taken] * float(how_many)
    elif coin_taken == "penny":
        how_many = input("How Many?: ")
        return payment[coin_taken] * float(how_many)
    else:
        return -2


def calculate_payment(required_payment, water, milk, coffee):
    payment_needed = required_payment
    payment_taken = 0
    change = 0
    refund = False

    while payment_taken < payment_needed:
        print("Needed: " + str(payment_needed))
        print("Received: " + str(payment_taken))
        action = take_money()
        if action == -2:
            print("Not a valid coin.")
        elif action == -1:
            refund = True
            break
        else:
            payment_taken += action

    if refund:
        print("You have received a Refund.")
    else:
        if payment_taken > payment_needed:
            change = payment_taken - payment_needed

        if change > 0:
            print("Now Pouring... Enjoy your Coffee!")
            print("You have received $" + str("{:.2f}".format(change)) + " in change.")
        else:
            print("Now Pouring... Enjoy your Coffee!")

        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        resources["money"] += required_payment








run_coffee_maker()




