av_water, av_milk, av_beans, av_cups, av_money = 400, 540, 120, 9, 550.0


def buy():
    global av_water, av_milk, av_beans, av_cups, av_money
    type_of_coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    if type_of_coffee == 1:  # espresso
        av_water -= 250
        av_beans -= 16
        av_money += 4
    elif type_of_coffee == 2:  # latte
        av_water -= 350
        av_milk -= 75
        av_beans -= 20
        av_money += 7
    elif type_of_coffee == 3:  # cappuccino
        av_water -= 200
        av_milk -= 100
        av_beans -= 12
        av_money += 6
    av_cups -= 1
    return av_water, av_milk, av_beans, av_cups, av_money


def fill():
    global av_water, av_milk, av_beans, av_cups

    add_water = int(input("Write how many ml of water do you want to add:\n"))
    add_milk = int(input("Write how many ml of milk do you want to add:\n"))
    add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    add_cups = int(input("Write how many disposable cups do you want to add:\n"))

    av_water += add_water
    av_milk += add_milk
    av_beans += add_beans
    av_cups += add_cups
    return av_water, av_milk, av_beans, av_cups


def take():
    global av_money
    print("I gave you ${}".format(av_money))
    av_money = 0
    return av_money


def results():
    global av_water, av_milk, av_beans, av_cups, av_money

    print(f"""
        The coffee machine has:
        {av_water}ml of water
        {av_milk}ml of milk
        {av_beans}g of coffee beans
        {av_cups} of disposable cups
        {av_money} of money""")


def select_action():
    action = input("Write action (buy, fill, take):\n")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    results()
