#https://newdigitals.org/2024/02/24/100-basic-python-codes/#list-files-in-a-directoryList Files in a Directory
#List Files in a Directory YOURPATH
# Import os module to read directory
import os
 
# Set the directory path
path = 'YOURPATH'
 
# Read the content of the file
files = os.listdir(path)
 
# Print the content of the directory
for file in files:
    print(file)
