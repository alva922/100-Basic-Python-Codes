# https://newdigitals.org/2024/02/24/100-basic-python-codes/#largest-number
# Program for finding the largest number in a list
mylist = [101, 62, 66, 45, 99, 18, 266, 18]
maxi = mylist[0]   # initializing maximum value
for i in mylist:
    if i > maxi:
        maxi = i
  
# printing the largest number
print("Largest number is:", maxi)
Output:
Largest number is: 266
