#https://newdigitals.org/2024/02/24/100-basic-python-codes/#read-write-w-pickle
#Read/Write w/ pickle
# Import pickle module
import pickle
 
# Declare the object to store data
dataObject = []
# Iterate the for loop for 5 times
for num in range(10,15):
   dataObject.append(num)
 
# Open a file for writing data
file_handler = open('numbers', 'wb')
# Dump the data of the object into the file
pickle.dump(dataObject, file_handler)
# close the file handler
file_handler.close()
 
# Open a file for reading the file
file_handler = open('numbers', 'rb')
# Load the data from the file after deserialization
dataObject = pickle.load(file_handler)
# Iterate the loop to print the data
for val in dataObject:
  print(val)
# close the file handler
file_handler.close()
 
Output:
file numbers  
10
11
12
13
14
