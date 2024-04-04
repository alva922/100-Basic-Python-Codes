#https://newdigitals.org/2024/02/24/100-basic-python-codes/#temperature-conversion
#Convert Celsius To Fahrenheit
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
#Example I/O
Enter temperature in celsius: 23
23.00 Celsius is: 73.40 Fahrenheit
#Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
#Example I/O
Enter temperature in fahrenheit: 100
100.00 Fahrenheit is: 37.78 Celsius
