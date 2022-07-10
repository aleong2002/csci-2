"""
Athena Leong
Assignment 9 Part 1
4/14/2022
"""
# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)
def valid_username(user):
    valid = True
    if len(user) < 5:
        valid = False
    
        
    if user.isalnum() == False:
        valid = False
    for i in user:
        if user[0].isdigit() == True:
            valid = False

    return valid


# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) must contain at least one lowercase letter
#             (4) must contain at least one uppercase letter
#             (5) must contain at least one number
# output:     boolean (True if valid, False if invalid)
def valid_password(pword):
    valid = True

    if len(pword) < 5:
        valid = False

    if pword.isalnum() == False:
        valid = False

    lower = 0
    upper = 0
    digit = 0
    for i in pword:
        if i.islower() == True:
            lower += 1
        if i.isupper() == True:
            upper += 1
        if i.isdigit() == True:
            digit += 1
    if lower < 1 or upper < 1 or digit <1:
        valid = False

    return valid



# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)
def username_exists(user):
    try:
        file = open("user_info.txt", "r")

    except:
        print("File cannot be opened")

    else:
        valid = False
        data = file.read()
        data = data.rstrip()
        file.close()

        lines = data.split("\n")
        
        for line in lines:

            splitline = line.split(",")

            if splitline[0] == user:
                valid = True
            
        return valid


# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)
def check_password(user, pword):
    try:
        file = open("user_info.txt", "r")

    except:
        print("File cannot be opened")

    else:
        data = file.read()
        data = data.rstrip()

        file.close()

        valid = False

        lines = data.split("\n")

        for line in lines:
            splitline = line.split(",")

            if username_exists(user) == True and splitline[1] == pword:
                valid = True

        return valid


# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)
def add_user(user, pword):
    try:
        file = open("user_info.txt", "a")

    except:
        print("File cannot be opened")

    else:
        valid = False
        if username_exists(user) == False:
            file.write(user)
            file.write(",")
            file.write(pword)
            file.write("\n")
            valid = True

            send_message("admin", user, "Welcome to your account!")
        file.close()
        return valid

         
        
# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
#
#             for example, if you call this function using the following arguments:
#
#             send_message('craig', 'pikachu', 'Hello there! nice to see you!')
#
#             the file 'messages/pikachu.txt' should gain an additional line data
#             that looks like the following:
#
#             craig|11/14/2020 12:30:05|Hello there! nice to see you!\n
#
#             note that you can generate the current time by doing the following:
#
#             import datetime
#             d = datetime.datetime.now()
#             month = d.month
#             day = d.day
#             year = d.year
#             ... etc. for hour, minute and second
#
#             keep in mind that you may need to 'append' to the correct messages file
#             since a user can receive an unlimited number of messages.  you may also
#             need to create a new message file if one does not exist for a user.
# output:     nothing
def send_message(sender, recipient, message):
    try:
        file = open(f"messages/{recipient}.txt", "a")

    except:
        print("File cannot be opened")

    else:
        import datetime
        d = datetime.datetime.now()
        month = d.month
        day = d.day
        year = d.year
        hour = d.hour
        minute = d.minute
        second= d.second
        
        file.write(sender)
        file.write("|")
        file.write(str(d.month))
        file.write("/")
        file.write(str(d.day))
        file.write("/")
        file.write(str(d.year))
        file.write(" ")
        file.write(str(d.hour))
        file.write(":")
        file.write(str(d.minute))
        file.write(":")
        file.write(str(d.second))
        file.write("|")
        file.write(message)
        file.write("\n")

        
        file.close()



# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.  assume you have this file named 'charmander.txt':
#
#             pikachu|11/14/2020 13:37:15|Hey there!
#             pikachu|11/14/2020 13:37:15|You too, ttyl
#
#             this function should generate the following output:
#
#             Message #1 received from pikachu
#             Time: 11/14/2020 13:37:15
#             Hey there!
#
#             Message #2 received from pikachu
#             Time: 11/14/2020 13:37:15
#             You too, ttyl
# output:     no return value (simply prints the messages)
def print_messages(user):
    try:
        file = open(f"messages/{user}.txt", "r")

    except:
        print("File cannot be opened")

    else:
        data = file.read()
        data = data.rstrip()

        file.close()

        lines = data.split("\n")

        messages = 0
        for line in lines:

            linesplit = line.split("|")
            messages += 1

            print(f"Message #{messages} received from {linesplit[0]}")
            print("Time:", linesplit[1])
            print(linesplit[2])
            print()



# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value
def delete_messages(user):
    try:
        file = open(f"messages/{user}.txt", "w")

    except:
        print("File cannot be opened")

    else:
        file.write("")
        file.close()


while True:

    choice = input("(l)ogin, (r)egister or (q)uit: ").lower()
    print()
    
    if choice == "r":
        print("Register for an account")
        
        uservalid = False
        pwordvalid = False
        exists = False
        user = input("Enter a username: ")
        pword = input("Enter a password: ")


        if valid_username(user) == True:
            uservalid = True

        if valid_password(pword) ==  True:
            pwordvalid = True

        if username_exists(user) == True:
            exists = True


        if uservalid == True:
            if pwordvalid == True:
                if exists == True:
                    print("Duplicate username, registration cancelled")

                else:
                    print("Registration successful!")
                    add_user(user, pword)
                    
            else:
                if exists == True:
                    print("Password is invalid, registration cancelled")
                    
                else:
                    print("Password is invalid, registration cancelled")
                        
        else:
            if pwordvalid == True:
                if exists == True:
                    print("Username is invalid, registration cancelled")
                    
                else:
                    print("Username is invalid, registration cancelled")
            else:
                if exists == True:
                    print("Username is invalid, registration cancelled")
                    
                else:
                    print("Username is invalid, registration cancelled")

        print()


    elif choice == "l":
        print("Log In")

        user = input("Username (case sensitive): ")
        pword = input("Password (case sensitive): ")

        if check_password(user, pword) == True:

            while True:
                print("You have been logged in successfully as", user)

                command = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ").lower()

                if command == "r":
                    try:
                        file = open(f"messages/{user}.txt", "r")
                        
                    except:
                        print("File cannot be opened")
                    else:
                        data = file.read()
                        file.close()
                        
                        if data == "":
                            print()
                            print("No messages in your inbox")
                            print()
                        else:
                            print()
                            print_messages(user)
                            print()
                            
                elif command == "s":
                    recipient = input("Username of recipient: ")
                    if username_exists(recipient) == False:
                        print("Unknown recipient")
                        print()
                        
                    else:
                        message = input("Type your message: ")
                        send_message(user, recipient, message)
                        print("Message sent!")
                        print()

                elif command == "d":
                    delete_messages(user)
                    print("Your messages have been deleted")
                    print()

                elif command == "l":
                    print("Logging out as username", user)
                    print()
                    break
                
                else:
                    print("This is an invalid choice")
        else:
            print("Cannot log in")



    elif choice == "q":
        print()
        print("Goodbye!")
        break

    else:
        print("This is an invalid choice")
