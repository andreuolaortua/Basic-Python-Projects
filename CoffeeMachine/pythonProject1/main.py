import machine_data
#Choice input
profit = 0
def check_resources(choice):
    #for choice in machine_data.MENU["ingredients"[]]:
    enough_resources = False
    for item in choice:
        if choice[item] > machine_data.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            for item in choice:
                machine_data.resources[item] -= choice[item]
            return True

    """if machine_data.MENU[choice["ingredients"["water"]]] > machine_data.resources["water"]:
        print("Sorry there is not enough water.")
    elif machine_data.MENU[choice["ingredients"["milk"]]] > machine_data.resources["milk"]:
        print("Sorry there is not enough milk.")
    elif machine_data.MENU[choice["ingredients"["coffee"]]] > machine_data.resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        enough_resources = True"""

def payment(choice):
    total_payment = False
    paid = float(input(f"The total amount is {choice["cost"]} Remeber to pay with quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01."))

    while total_payment == False:
        if paid >= choice["cost"]:
            change = paid-choice["cost"]
            global profit
            profit += choice["cost"]
            print(f"Thanks! The change is {change}.")
            total_payment = True
        else:
            paid += float(input("You need to insert more money."))
    return total_payment



def coffie_machine():

    is_on = True

    while is_on:

        choice = input("What would you like? espresso, latte or cappuccino? ")
        if choice == "off":
            is_on = False    #Check which is the choice
        elif choice == "report":
            print(f"Water: {machine_data.resources["water"]}ml")
            print(f"Milk: {machine_data.resources["milk"]}ml")
            print(f"Coffee: {machine_data.resources["coffee"]}g")
            print(f"Money: ${profit}")
        else:
            print(f"Current resources values of {choice}")
            print(f"{machine_data.MENU[choice]}")
            drink = machine_data.MENU[choice]
            if check_resources(drink["ingredients"]):
                payment(drink)
                print(f"Here is your {choice}. Enjoy!")
                False
        #coffie_machine


coffie_machine()