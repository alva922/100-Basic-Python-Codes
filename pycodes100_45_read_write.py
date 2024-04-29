#https://newdigitals.org/2024/02/24/100-basic-python-codes/#read-write-files
#Read/Write Files
#Assign the filename
filename = "names.txt"
# Open file for writing
fileHandler = open(filename, "w")
 
# Add some text
fileHandler.write("Ram\n")
fileHandler.write("John\n")
fileHandler.write("David\n")
 
# Close the file
fileHandler.close()
 
# Open file for reading
fileHandler = open(filename, "r")
 
# Read a file line by line
for line in fileHandler:
  print(line)
  
# Close the file
fileHandler.close()
 
Output:
Ram
 
John
 
David
