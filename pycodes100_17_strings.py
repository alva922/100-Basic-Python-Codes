#https://newdigitals.org/2024/02/24/100-basic-python-codes/#using-strings
#Working with strings: objects that contain sequences of character data.
name="john"+" "+"smith"
print(name.title())
print("Hello {},you are {} years old".format(name.title(),28))
print(f"Hello {name.title()}")
print("It is {},he is {} years old and his name is  {}!".format(False,28,"John Smith".title()))
print(name.replace("john smith","Said ZITOUNI"))
 
Output:
John Smith
Hello John Smith,you are 28 years old
Hello John Smith
It is False,he is 28 years old and his name is  John Smith!
Said ZITOUNI
 
name="john"+" "+"smith"
print(name.replace("john smith","Said ZITOUNI"))
print(name.upper())
print(name.find("ohn"))
print(name.strip())
list=name.split(" ")
print(list)
s="$$John"
print(s.lstrip('$'))
 
Output:
Said ZITOUNI
JOHN SMITH
1
john smith
['john', 'smith']
John
#Read more about strings here
#https://realpython.com/python-strings/
