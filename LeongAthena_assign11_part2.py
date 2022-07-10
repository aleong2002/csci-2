"""
Athena Leong
Assignment 11 Part 2
4/28/22
"""
# KAPP_ASSIGNMENT11_PART2

class Smartphone:

    # construct a new Smartphone
    # smartphones need to keep track of how much space they have left (integer)
    # they also need to keep track of their name (string)
    # smartphones will need some kind of internal system to keep track of all of 
    # the apps that are installed, along with their size.  a list or a dictionary
    # would be useful here.
    # when a phone is constructed the 'report' method should be called (see below)
    # this method returns nothing and simply prints the desired output to the user
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.name = name

        # store apps and their sizes
        self.apps = {}

        # when constructed, print report
        print("Smartphone created!")
        self.report()
        
    # add a new app to the smartphone given an appname (string) and an appsize (integer)
    # if any of the following conditions are detected the method should reject the input
    # and print out a message as to why the app cannot be installed:
    # (1) the app is already installed
    # (2) the phone cannot hold any additional apps because the capacity has been reached
    # (3) the app size is negative
    # this method returns nothing and simply prints the desired output to the user
    def add_app(self, appname, appsize):
        remaining = self.capacity
        for i in self.apps:
            remaining -= self.apps[i]
            
        if appname in self.apps:
            print("Cannot add app: already installed")

        elif appsize < 0:
            print("Cannot add app: size cannot be negative")

        elif appsize > remaining:
            print("Cannot add app: not enough available space")

        else:
            self.apps[appname] = appsize
            print("App", appname, "was added successfully")
        
    # removes an app from the phone based on appname (string)
    # if the app is not installed, reject it and print out an error message
    # this method returns nothing and simply prints the desired output to the user
    def remove_app(self, appname):
        if appname not in self.apps:
            print("Cannot remove app: app not currently installed")

        else:
            del self.apps[appname]
            print("App", appname, "was removed successfully")
            
    # resets the phone (removes all apps, gives the phone a name of "Untitled")
    # print out a confirmation message
    def reset(self):
        self.name = "Untitled"
        self.apps.clear()

        print("Phone has been reset")
        
    # renames the phone
    # print out a confirmation message
    def rename(self, new_name):
        self.name = new_name
        print("Phone has been renamed")
        
    # checks to see if an app is installed based on appname (string)
    # returns True if the app is installed, False if it is not
    def has_app(self, appname):
        if appname in self.apps:
            return True

        else:
            return False
        
    # returns the current space available on the phone (integer)
    def get_available_space(self):
        remaining = self.capacity
        for i in self.apps:
            remaining -= self.apps[i]

        print("Available space:", remaining, "GB")
        
    # prints a detailed report that describes the following:
    # Name of phone
    # Storage capacity of phone
    # Used space
    # Available space
    # # of apps installed
    # a listing of all apps installed, in alphabetical order, with their sizes
    # this method returns nothing and simply prints the desired output to the user
    def report(self):
        print("Name:", self.name)
        print("Storage capacity:", self.capacity, "GB")

        remaining = self.capacity
        for i in self.apps:
            remaining -= self.apps[i]
            
        print("Used space:", self.capacity - remaining, "GB")
        print("Available space:", remaining, "GB")
        print("Apps installed:", len(self.apps))

        for i in sorted(self.apps):
            print(f"* {i} ({self.apps[i]} GB)")
        

"""
a = Smartphone(128, "Athena's phone")
a.add_app("Instagram", 10)
a.add_app("Twitter", 12)
a.report()
a.has_app("Twitter")
a.has_app("Hulu")
a.get_available_space()
a.report()
a.remove_app("Instagram")
a.report()
a.rename("Jeno's phone")
a.reset()
a.report()
"""
while True:
    
    try:
        capacity = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
    
    except:
        print("Invalid size, try again")
    else:
        if capacity == 32 or capacity == 64 or capacity == 128:
            break
        else:
            print("Invalid size, try again")

            
name = input("Smartphone name: ")
a = Smartphone(capacity, name)
    
print()
while True:
    command = input("(r)eport, (a)dd app, r(e)move app, re(s)et, re(n)ame or (q)uit: ").lower()

    if command == "r":
        a.report()

    elif command == "a":
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))
        
        a.add_app(appname, appsize)

    elif command == "e":
        appname = input("App name to remove: ")
        a.remove_app(appname)

    elif command == "s":
        a.reset()

    elif command == "n":
        name = input("Enter a new name for your phone: ")
        a.rename(name)

    elif command == 'q':
        print("Goodbye!")
        break

    else:
        print("This command is invalid")
    print()
