#https://newdigitals.org/2024/02/24/100-basic-python-codes/#bmi-calculator
# BMI Calculator
Height = float(input('Enter your Height in centimeters: '))
Weight = float(input('Enter your Weight in Kg: '))
Height = Height/100
BMI = Weight/(Height*Height)
print('your Body Mass Index is: ', BMI)
if(BMI > 0):
    if(BMI <= 16):
        print('you are severely underweight')
    elif(BMI <= 18.5):
        print('you are underweight')
    elif(BMI <= 25):
        print('you are Healthy')
    elif(BMI <= 30):
        print('you are overweight')
    else:
        print('you are severely overweight')
else:
    print('Enter valid details')

#Example I/O
Enter your Height in centimeters: 180
Enter your Weight in Kg: 90
your Body Mass Index is:  27.777777777777775
you are overweight
