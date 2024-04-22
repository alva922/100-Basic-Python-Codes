#https://newdigitals.org/2024/02/24/100-basic-python-codes/#use-of-regex
#Use of regex
!pip install re
# Import re module
import re
 
# Take any string data
string = input("Enter a string value: ")
# Define the searching pattern
pattern = 'Ale'
 
# match the pattern with input value
found = re.match(pattern, string)
 
# Print message based on the return value
if found:
  print("The input value is started with the capital letter")
else:
  print("You have to type string start with the capital letter")

#Example I/O
Enter a string value: Alessandro
The input value is started with the capital letter
