# https://newdigitals.org/2024/02/24/100-basic-python-codes/#pizza-deliveries
#Pizza Deliveries
# Implementing the Pizza Deliveries chatbot
print("===================================")
print("WELCOME TO PYTHON PIZZA DELIVERIES!")
print("===================================\n")
total_bill = 0
 
def pizza_size():
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25
    global total_bill
    size = str(input("What size pizza do you want? S, M, or L ")).upper()
    if size == "S":
        total_bill += small_pizza
        print("You want a small pizza.")
        print("-----------------------\n")
        pepperoni(size)
    elif size == "M":
        total_bill += medium_pizza
        print("You want a medium pizza.")
        print("------------------------\n")
        pepperoni(size)
    elif size == "L":
        total_bill += large_pizza
        print("You want a large pizza.")
        print("-----------------------\n")
        pepperoni(size)
    else:
        print("Please respond with S, M, or L")
        print("------------------------------\n")
        pizza_size()
 
def pepperoni(size):
    sml_pep = 2
    med_lar_pep = 3
    global total_bill
    add_pepperoni = str(input("Do you want pepperoni? Y or N ")).upper()
    if size == "S" and add_pepperoni == "Y":
        total_bill += sml_pep
        print("You want pepperoni.")
        print("-------------------\n")
        extra_cheese()
    elif (size == "M" or "L") and add_pepperoni == "Y":
        total_bill += med_lar_pep
        print("You want pepperoni.")
        print("-------------------\n")
        extra_cheese()
    elif add_pepperoni == "N":
        print("You don't want pepperoni.")
        print("-------------------------\n")
        extra_cheese()
    else:
        print("Please respond with Y or N")
        print("--------------------------\n")
        pepperoni(size)
 
def extra_cheese():
    add_cheese = 1
    global total_bill
    more_cheese = str(input("Do you want extra cheese? Y or N ")).upper()
    if more_cheese == "Y":
        total_bill += add_cheese
        print("You want extra cheese.")
        print("----------------------\n")
        print(f"Your final bill is: ${total_bill}.")
    elif more_cheese == "N":
        print("You don't want extra cheese.")
        print("----------------------------\n")
        print(f"Your final bill is: ${total_bill}.")
    else: 
        print("Please respond with Y or N")
        print("--------------------------\n")
        extra_cheese()
 
pizza_size()
#Example I/O
===================================
WELCOME TO PYTHON PIZZA DELIVERIES!
===================================
 
What size pizza do you want? S, M, or L L
You want a large pizza.
-----------------------
 
Do you want pepperoni? Y or N Y
You want pepperoni.
-------------------
 
Do you want extra cheese? Y or N Y
You want extra cheese.
----------------------
 
Your final bill is: $29.
