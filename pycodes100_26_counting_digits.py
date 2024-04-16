# https://newdigitals.org/2024/02/24/100-basic-python-codes/#counting-digits
# Counting Digits
num=int(input("Enter number: "))
count=0
i = num
# count the digits
while(i>0):
    count=count+1
    i=i//10
print(f"The number of digits in {num}:",count)
#Example I/O
Enter number: 1000
The number of digits in 1000: 4
