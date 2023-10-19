##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""


import time
q = "Enter a username: "
q1 = "Enter a password: "
a = str(input(q))
a1 = str(input(q1))
count = 0
while (count < 2 and a != "admin") or (count < 2 and a1 != "12345"):
    time.sleep(1/2)
    count += 1
    print(count)
    print("Access denied")
    a = str(input(q))
    a1 = str(input(q1))
if a == "admin" and a1 == "12345":
    print("Access Granted")
else:
    print("Too many failed attempts. Access denied")
count = 0