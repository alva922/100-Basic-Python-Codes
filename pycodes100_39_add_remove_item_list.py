#https://newdigitals.org/2024/02/24/100-basic-python-codes/#add-remove-the-item-from-a-list
#Add/Remove the Item from a List
# Declare a fruit list
fruits = ["Mango","Orange","Guava","Banana"]
 
# Insert an item in the 2nd position
fruits.insert(1, "Apple")
 
# Displaying list after inserting
print("The fruit list after insert:")
print(fruits)
  
# Remove an item
fruits.remove("Banana")
 
# Print the list after delete
print("The fruit list after delete:")
print(fruits)
 
Output:
The fruit list after insert:
['Mango', 'Apple', 'Orange', 'Guava', 'Banana']
The fruit list after delete:
['Mango', 'Apple', 'Orange', 'Guava']
