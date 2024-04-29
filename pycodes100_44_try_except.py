#https://newdigitals.org/2024/02/24/100-basic-python-codes/#using-try-except-blocks
#Using Try-Except Blocks
# Try block
try:
    # Take a number
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
 
# Exception block    
except (ValueError):
  # Print error message
  print("Enter a numeric value")
