
store = {
    "Water": 10000,
    "Milk":10000,
    "Coffee": 1000,
    "Money": 0
}
def coffe_machine():
    global store
    price = {
        "espresso": {
            "price": 1.50,
            "Water": 50,
            "Milk":0,
            "Coffee": 18,
        },
        "latte": {
            "price": 2.50,
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cappuccino": {
            "price": 3.00,
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        }
    }
    is_finished = False
    while not is_finished:
        choice = input("“What would you like? (espresso/latte/cappuccino): \n").lower() # report off espresso latte cappuccino
        if choice not in ['espresso', 'latte', 'cappuccino', "report", "off"]:
            print("Please type correct name ")
            continue
        if choice == 'off': 
            print("Thank you. Machine turned off")
            break
        elif choice == 'report':
            print(f"Water: {store['Water']}")
            print(f"Milk: {store['Milk']}")
            print(f"Coffee: {store['Coffee']}")
            print(f"Money: {store['Money']}")
            continue

        if not( store["Coffee"] >= price[choice]['Coffee'] and store["Milk"]>=price[choice]["Milk"] and store["Water"]>=price[choice]["Water"]):
            print("Sorry there is not enough ingredients.")
            break
        while True:
            try: 
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total = quarters * 0.25 + dimes * 0.1 + nickels * 0.005 + pennies * 0.001 # total price ${}
                change = 0
                if total > price[choice]["price"]:
                    change = total - price[choice]["price"]
                    store["Money"] += price[choice]["price"]
                    print(f"Here is ${change} in change.")
                    print(f"Enjoy your {choice}")
                    break
                elif total < price[choice]['price']:
                    print("Not enough money")
                    print("Here your coins back")
                    break
                else: 
                    store["Money"] += price[choice]["price"]
                    print(f"Enjoy your {choice}")
            except ValueError:
                print('Please enter a numeric value for coins count. ')
                continue
        is_finished = True
        


coffe_machine()   


        
