#https://newdigitals.org/2024/02/24/100-basic-python-codes/#email-slicer
#Trying the Email Slicer that will take an email address as input and slice it to produce the username and the domain associated with it.
email = input("Enter Your Email: ").strip()
 
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
 
print(f"Your username is {username} & domain is {domain}")
#Example I/O
Enter Your Email: metava922@gmail.com
Your username is metava922 & domain is gmail.com
