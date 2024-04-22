#https://newdigitals.org/2024/02/24/100-basic-python-codes/#use-of-getpass
#Use of getpass
# import getpass module
import getpass
 
# Take password from the user
passwd = getpass.getpass('Password:')
 
# Check the password
if passwd == "python":
    print("You are verified")
else:
    print("You are not verified")

#Example I/O
Password:········
You are verified
