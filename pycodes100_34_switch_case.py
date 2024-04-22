#https://newdigitals.org/2024/02/24/100-basic-python-codes/#switch-case-statement
#Switch Case Statement
# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "5006": "Employee Name: John",
        "5008": "Employee Name: Ram",  
        "5010": "Employee Name: Mohamend",
    }
    '''The first argument will be returned if the match found and
        employee ID does not exist will be returned if no match found'''
    return switcher.get(ID, "employee ID does not exist")
 
# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))
 
Output:
Enter the employee ID: 5008
Employee Name: Ram
