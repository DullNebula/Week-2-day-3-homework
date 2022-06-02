#1. Build a shopping car
#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list
#Welcome to amazong
import math
item_stock = {
    'small water' :("Small Water", 2.50),
    'medium water' : ("Medium Water", 4.50),
    'large water' : ("Large Water", 6.00),
    'water case' : ("Water Case", 10.00),
    'model car' : ("Model Car", 25.00),
    'model tank' : ("Model Tank", 30.00),
    'model plane' : ("Model Plane", 28.00),
    'hammer' : ("Hammer", 8.00),
    'screwdriver' : ("Screwdriver", 5.50),
    'pliers' : ("Pliers", 4.20),
    'pasta' : ("Pasta", 5.00),
    'sausage': ("Sausage", 5.50),
    'hard drive': ("Hard Drive", 50.00),
    'sd card' : ("SD Card", 75.00)
}
for small_name, (pretty_name, price) in item_stock.items():
    print(f"{pretty_name}: ${price:.2f}")


cart_list = []

#function for printing cart
def print_cart_nice(cart):
    for item in cart:
        pretty_name, price = item_stock[item]
        print(f"{pretty_name}: ${price:.2f}")


while True:
    cart_item = input("Please enter an item to add to your cart. Enter 'Quit' when finished, or 'Cart' to view your cart or 'remove item' to delete a selection\n")
    cart_item = cart_item.lower()
    cart_item = cart_item.strip()
    if cart_item == "quit":
        total_cost = sum([item_stock[item][1] for item in cart_list])
        print(f"Your final cart consists of: ")
        print_cart_nice(cart_list)
        print(f"Total cost: ${total_cost:.2f}")
        break
    if cart_item == "cart":
        print(f"Your cart currently has: ")
        print_cart_nice(cart_list)
        continue
    if cart_item in item_stock:
        cart_list.append(cart_item)
    else:
        print(f"Sorry, we do not have {cart_item}")
    if cart_item == "remove item":
        print("What item would you like to remove?\n")
        print_cart_nice(cart_list)
        delete_item = input()
        delete_item = delete_item.lower()
        delete_item = delete_item.strip()
        if delete_item not in cart_list:
            print(f"{delete_item} is not in your cart or your selection was misspelled.\n")
        else: cart_list.remove(delete_item), print(f"{delete_item} has been removed!\n")

        


