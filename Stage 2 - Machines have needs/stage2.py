def quantity(ingredient):
    return ingredient * int(num_cups)


num_cups = input("Write how many cups of coffee you will need:\n")
water, milk, coffee = 200, 50, 15

print("""
For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans
""".format(num_cups, quantity(water), quantity(milk), quantity(coffee)))
