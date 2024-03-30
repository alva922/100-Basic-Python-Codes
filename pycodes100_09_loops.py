#https://newdigitals.org/2024/02/24/100-basic-python-codes/#practicing-loops
#Practicing Loops
#While_loop
names=["Bob","Jack","Bob","Alpha","Astra","Bob"]
n=names.count("Bob")
while n>1:
    names.remove("Bob")
    n-=1
print(names)
['Jack', 'Alpha', 'Astra', 'Bob']

#for Loop example
languages = ['Swift', 'Python', 'Go']
 
# access elements of the list one by one
for i in languages:
    print(i)
Swift
Python
Go
