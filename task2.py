#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
import time
q = "Enter a username: "
q1 = "Enter a password: "
a = str(input(q))
a1 = str(input(q1))

while a != "admin" or a1 != "12345":
    time.sleep(1/2)
    print("Access denied")
    a = str(input(q))
    a1 = str(input(q1))
else:
    print("Access Granted")