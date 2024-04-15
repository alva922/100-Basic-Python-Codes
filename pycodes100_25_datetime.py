#https://newdigitals.org/2024/02/24/100-basic-python-codes/#datetime-module
# Datetime Module
import datetime
# Create a date object for January 1, 2023
d = datetime.date(2023, 1, 1)
print(d)  
# Get the current date
today = datetime.date.today()
print(today) 
# Get the year, month, and day of a date object
year = today.year
month = today.month
day = today.day
print(year, month, day)  # print each value separately
# Format a date object as a string
date_string = today.strftime("%d/%m/%Y")
print(date_string) 
# Parse a date string into a date object
date_string = "2023-03-15"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print(parsed_date) 
# Get the day of the week as an integer (Monday is 0 and Sunday is 6)
weekday = today.weekday()
print(weekday)

Output:
2023-01-01
2024-02-20
2024 2 20
20/02/2024
2023-03-15
1
# Let’s take an example of the time class

import datetime
# Create a time object for 9:30 AM
t = datetime.time(9, 30)
print(t)  
# Get the current time
now = datetime.datetime.now()
current_time = now.time()
print(current_time)  
# Get the hour, minute, and second of a time object
hour = t.hour
minute = t.minute
second = t.second
print(hour, minute, second)  # print each value separately
# Format a time object as a string
time_string = t.strftime("%I:%M %p")
print(time_string)  
# Compare two time objects
time1 = datetime.time(8, 30)
time2 = datetime.time(9, 30)
if time1 < time2:
    print("time1 is earlier than time2")
else:
    print("time1 is late than time2")

# Output
09:30:00
21:25:29.116006
9 30 0
09:30 AM
time1 is earlier than time2
