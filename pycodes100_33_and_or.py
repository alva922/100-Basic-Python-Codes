#https://newdigitals.org/2024/02/24/100-basic-python-codes/#using-and-or-operators
#Using AND/OR Operators
#Example of using AND and OR operators
# Take practical marks
x = float(input("Enter the Practical marks: "))
# Take theory marks
y = float(input("Enter the Theory marks: "))
 
# Check the passing condition using AND and OR operator
if (x >= 25 and y >= 45) or (x + y) >=70:
    print("\nYou have passed")
else:
    print("\nYou have failed")
#Example I/O
Enter the Practical marks: 30
Enter the Theory marks: 40
 
You have passed  
