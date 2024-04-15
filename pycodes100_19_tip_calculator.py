#https://newdigitals.org/2024/02/24/100-basic-python-codes/#tip-calculator
# Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
 
print("Welcome to the Tip Calculator")
 
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))
 
tip = bill * (percentage / 100)
total_bill = bill + tip
individual_amount = total_bill / people_count
final_amount = format(individual_amount, '.2f')
 
print(f"Each person should pay ${final_amount}")
#Example I/O
Welcome to the Tip Calculator
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay $33.60
