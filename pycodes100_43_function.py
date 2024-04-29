#https://newdigitals.org/2024/02/24/100-basic-python-codes/#define-and-call-a-function
#Define and Call a Function
# Define addition function
def addition(number1, number2):
    result = number1 + number2
    print("Addition result:",result)
 
# Define area function with return statement
def area(radius):
    result = 3.14 * radius * radius
    return result  
 
# Call addition function
addition(5, 3)
# Call area function
print("Area of the circle is",area(2))
 
Output:
Addition result: 8
Area of the circle is 12.56
