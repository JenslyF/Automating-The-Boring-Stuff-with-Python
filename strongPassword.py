# Strong Password Detection

import re

# Typed Password
TypedPasswd = input('Type your Password: ')

# Password must be at least eight characters long, contains both lowercase and uppercase characters
# and has at least one digit
StrongPass = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-z\d]{8,}$', TypedPasswd)

# Check to see if that shit matches
# it has one issue, it doesn't check if the password is right for more than one iteration

while True:
    if StrongPass:
        print('Your password matches. Thank you!')
        break
    else:
        TypedPasswd = input('Wrong Password, Try Again: ')
        StrongPass = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-z\d]{8,}$', TypedPasswd)


