water, milk, beans, cups, money = 400, 540, 120, 9, 550


def show_state():
    print()
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"${money} of money")


def main_menu():
    return input("Write action (buy, fill, take, remaining, exit):\n")


def choose_coffee_type():
    print()
    return input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")


def enough_resources():
    print("I have enough resources, making you a coffee!")


def not_enough_water():
    print("Sorry, not enough water!")


def not_enough_milk():
    print("Sorry, not enough milk!")


def not_enough_beans():
    print("Sorry, not enough coffee beans!")


def fill():
    global water, milk, beans, cups
    print()
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups do you want to add:\n"))


def take():
    global money
    print("I gave you ${}".format(money))
    money = 0
    return money


def main():
    action = ""
    while action != "exit":

        action = main_menu()

        if action == "buy":
            global water, milk, beans, cups, money
            print()
            coffee_type = choose_coffee_type()
            if coffee_type == "back":
                continue
            coffee_type = int(coffee_type)
            if cups > 0:
                if coffee_type == 1:  # espresso
                    if water >= 250 and beans >= 16:
                        enough_resources()
                        water -= 250
                        beans -= 16
                        money += 4
                        cups -= 1
                    else:
                        if water < 250:
                            not_enough_water()
                            continue
                        else:
                            not_enough_beans()
                            continue

                elif coffee_type == 2:  # latte
                    if water >= 350 and milk >= 75 and beans >= 20:
                        enough_resources()
                        water -= 350
                        milk -= 75
                        beans -= 20
                        money += 7
                        cups -= 1
                    else:
                        if water < 350:
                            not_enough_water()
                        if milk < 75:
                            not_enough_milk()
                        if beans < 20:
                            not_enough_beans()

                elif coffee_type == 3:  # cappuccino
                    if water >= 200 and milk >= 100 and beans >= 12:
                        enough_resources()
                        water -= 200
                        milk -= 100
                        beans -= 12
                        money += 6
                        cups -= 1
            else:
                print("Sorry, not enough cups!")

        elif action == "fill":
            fill()
            print()
        elif action == "take":
            take()
            print()
        elif action == "remaining":
            show_state()
            print()


main()
