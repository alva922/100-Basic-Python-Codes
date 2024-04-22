#https://newdigitals.org/2024/02/24/100-basic-python-codes/#add-and-search-data-in-the-set
#Add and search data in the set by defining the number set
# Define the number set
numbers = {13, 10, 56, 18, 12, 44, 87}
  
# Add a new data
numbers.add(63)
# Print the set values
print(numbers)
 
message = "Number is not found"
 
# Take a number value for search
search_number = int(input("Enter a number:"))
# Search the number in the set
for val in numbers:
    if val == search_number:
        message = "Number is found"
        break
 
print(message)

#Example I/O
{18, 87, 56, 10, 12, 13, 44, 63}

Enter a number:10
Number is found
