#https://newdigitals.org/2024/02/24/100-basic-python-codes/#working-with-lists
#Working with Lists
a=[14,15,"Said"]
b=[14,58,56]
b_copy=b[:]
c=a+b
print(c)
print("a:{} and b:{}".format(a,b))
print("a's location is {}, b's location is {}.".format(id(a),id(b)))
a[0]=165
print("a's location is {}, b's location is {}.".format(id(a),id(b)))
print(b_copy)
family=["Said","Maureen","Mina","Fatima"]
print("first letter of each one: {},{},{},{}".format(family[0][0],family[1][0],family[2][0],family[3][0]))

#Example I/O

[14, 15, 'Said', 14, 58, 56]
a:[14, 15, 'Said'] and b:[14, 58, 56]
a's location is 2582634989888, b's location is 2582634988736.
a's location is 2582634989888, b's location is 2582634988736.
[14, 58, 56]
first letter of each one: S,M,M,F

