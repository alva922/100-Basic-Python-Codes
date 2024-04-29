#https://newdigitals.org/2024/02/24/100-basic-python-codes/#use-of-map-function
#Use of map Function
#Example of calculating the x to the power n using map()
# Define the function to calculate power
def cal_power(n):    
    return x ** n
 
# Take the value of x
x = int(input("Enter the value of x:"))
# Define a tuple of numbers
numbers = [2, 6, 3]
 
# Calculate the x to the power n using map()
result = map(cal_power, numbers)
print(list(result))
