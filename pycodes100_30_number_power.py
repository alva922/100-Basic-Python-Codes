#https://newdigitals.org/2024/02/24/100-basic-python-codes/#raise-a-number-to-a-power
#Raise a number to a power using math
#!pip install math
import math
# Assign values to a and n
a = 4
n = 3
 
# Method 1
b = a ** n
print("%d to the power %d is %d" % (a,n,b))
 
# Method 2
b = pow(a,n)
print("%d to the power %d is %d" % (a,n,b))
 
# Method 3
b = math.pow(a,n)
print("%d to the power %d is %5.2f" % (a,n,b))
 
Output:
4 to the power 3 is 64
4 to the power 3 is 64
4 to the power 3 is 64.00
