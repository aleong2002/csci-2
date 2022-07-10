"""
Athena Leong
Assignment #7 Pt 1
3/31/22
"""
# KAPP_ASSIGNMENT07_PART1
while True:
    # ask for username
    username = input("Enter a username: ")

    # assume username is valid
    valid = True
    length = len(username)
    print("* Length of username:", length)
    if length < 8 or length > 15:
        print("  ERROR - username must be between 8 and 15 characters long")
        valid = False
    print("* All characters are alphabetic or numeric:", username.isalnum())
    if username.isalnum() == False:
        print("  ERROR - username must be alphanumeric")
        valid = False
    print("* First character is a digit:", username[0].isdigit())
    if username[0].isdigit() == True:
        print("  ERROR - first character cannot be a digit")
        valid = False
    print("* Last character is a digit:", username[-1].isdigit())
    if username[-1].isdigit() == True:
        print("  ERROR - last character cannot be a digit")
        valid = False

    upper = 0
    digit = 0
    lower = 0
    for c in username:
        if c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isupper():
            upper += 1

    print("* # of uppercase characters:", upper)
    if upper == 0:
        print("  ERROR - username must contain at least one uppercase character")
        valid = False

    print("* # of lowercase characters:", lower)
    if lower == 0:
        print("  ERROR - username must contain at least one lowercase character")
        valid = False

    print("* # of digit characters:", digit)
    if digit == 0:
        print("  ERROR - username must contain at least one digit character")
        valid = False
    if valid == True:
        print("Username is valid!")
        break
    else:
        print("Username is not valid, please try again")
        print()
print()

# password loop
while True:
    password = input("Enter a password: ")
    # assume valid
    valid = True

    print("* Length of password:", len(password))
    if len(password) < 8:
        print("  ERROR - password must be at least 8 characters long")
        valid = False

    if username in password:
        user = True
    else:
        user = False
        
        
    print("* Username is part of password:", user)
    if password.find(username) != -1:
        print("  ERROR - username cannot exist within password")

    upper = 0
    digit = 0
    lower = 0
    special = 0
    invalid = 0
    for c in password:
        if c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isupper():
            upper += 1
        elif c == "#" or c == "$" or c == "%" or c == "!":
            special += 1
        else:
            invalid += 1


    print("* # of uppercase characters in the password:", upper)
    print("* # of lowercase characters in the password:", lower)
    print("* # of digit characters in the password:", digit)
    if upper == 0:
        print("  ERROR - password must contain at least one uppercase character")
        valid = False
    if lower == 0:
        print("  ERROR - password must contain at least one lowercase character")
        valid = False
    if digit == 0:
        print("  ERROR - password must contain at least one digit character")
        valid = False
    
    print("* # of special characters in the password:", special)
    if special == 0:
        print("  ERROR - password must contain at least one special character")
        valid = False

    print("* # of invalid characters in the password:", invalid)
    if invalid != 0:
        print("  ERROR - password cannot contain any invalid characters")
        valid = False

    if valid == True:
        print("Password is valid!")
        break
    else:
        print("Password is not valid, please try again")
        print()
