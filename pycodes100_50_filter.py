#https://newdigitals.org/2024/02/24/100-basic-python-codes/#use-of-filter-function
#Use of filter Function
# Define a list of participant
participant = ['Ram', 'John', 'David', 'Krishna', 'Prasad']
# Define the function to filters selected candidates
def SelectedPerson(participant):
    selected = ['John', 'Rahman', 'Ram']
    if(participant in selected):
        return True
selectedList = filter(SelectedPerson, participant)
print('The selected candidates are:')
for candidate in selectedList:
    print(candidate)
 
Output:
The selected candidates are:
Ram
John
