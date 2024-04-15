# https://newdigitals.org/2024/02/24/100-basic-python-codes/#paint-area-calculator
# Paint Area Calculator
# Program which calculates how many cans of paint are needed to paint a wall (1 can of paint can cover 5 square meters of a wall)
import math
 
# 1 can of paint can cover 5 square meters of a wall. 
def paint_calc(height, width, cover):
    number_of_cans = int(math.ceil((height * width) / cover))
    print(f"You'll need {number_of_cans} cans of paint.")
 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
 
paint_calc(height=test_h, width=test_w, cover=coverage)
#Example I/O
Height of wall: 3
Width of wall: 5
You'll need 3 cans of paint.
