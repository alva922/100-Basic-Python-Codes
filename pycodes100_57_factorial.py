#Defining the function factorial_of_number
def factorial_of_number(n):
    if n < 0:
        raise ValueError("The Number you entered is less than 0")
    if n is 1:
        return 1
    elif n is 0:
        return 1
    else:
        return n * factorial_of_number(n-1)
#Example I/O
print(factorial_of_number(6))
720 
