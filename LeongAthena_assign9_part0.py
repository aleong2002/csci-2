"""
Athena Leong
Assignment 9 Part 0
4/14/2022
"""
# TASK #1
print("NYU Computer Science Registration System")

# ask for the course number
course = input("Enter a course: ").upper()

# try block to avoid exceptions
try:
    file = open("class_data.txt", "r")

except:
    print("File cannot be opened")

else:
    # read data
    data = file.read()
    data = data.rstrip()

    # close file when done
    file.close()

    # parse into course name and description
    lines = data.split("\n")

    # loop to separate into smaller list of lines
    found = False
    for line in lines:
        splitline = line.split(",")

        # if the course matches with the  course in list, change value to True
        if course == splitline[0]:
            print("The title of this class is:", splitline[1])
            found = True

    # if not found
    if found == False:
        print("That course is not running this semester")

    # TASK #2
    # if found, get the students enrolled 
    else:

        # read enrollment data
        try:
            file = open("enrollment_data.txt", "r")

        except:
            print("File cannot be opened")

        else:
            enrolldata = file.read()
            data = data.rstrip()

            # file close
            file.close()

            elines = enrolldata.split("\n")

            # add students when found
            students = 0
            regstudents = ""
            for item in elines:

                itemsplit = item.split(",")
                if itemsplit[0] == course:
                    students += 1
                    regstudents += f"* {itemsplit[1]},{itemsplit[2]}\n"

            print("The course has", students, "students enrolled")
            print(regstudents)
