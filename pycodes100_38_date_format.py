#https://newdigitals.org/2024/02/24/100-basic-python-codes/#use-of-date-format
#Use of Date Format
#!pip install datetime
from datetime import date
 
# Read the current date
current_date = date.today()
 
# Print the formatted date
print("Today is :%d-%d-%d" % (current_date.day,current_date.month,current_date.year))
 
# Set the custom date
custom_date = date(2026, 12, 26)
print("The date is:",custom_date)
 
Output:
Today is :23-2-2024
The date is: 2026-12-26
