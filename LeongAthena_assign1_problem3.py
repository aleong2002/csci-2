"""
Assignment #3: Problem #3
Athena Leong
1/28/2022
Section 04
LeongAthena_assign1_part3
"""
# ask for 3 name inputs stored into variables
nameun = input("Please enter name #1: ")
namedeux = input("Please enter name #2: ")
nametrois = input("Please enter name #3: ")
print()

"""
print header and line break after a border of dashes
"""
print("Here are your names in every possible order:")
print("--------------------------------------------")
print()

"""
print names in order of input with commas
use sep="" to remove spaces, only adding the necessary ones back in with arguments
"""
print("1. ", nameun, ", ", namedeux, ", ", nametrois, sep="")
print()

"""
list first, third, and scond name respectively, but replace spaces with **
manually add spaces back in between the **'s
"""
print("2. ", nameun, " ", nametrois, " ", namedeux, " ", sep="**")
print()

"""
print 2nd, 1st, and 3rd name respectively and remove spaces
insert dashes as string arguments
"""
print("3. ", namedeux,"-", nameun,"-", nametrois, sep="")
print()

"""
print 2nd name individually with "4."
then print 3rd and 1st names on their lines
"""
print("4.", namedeux)
print(nametrois)
print(nameun)
print()

"""
print 3rd name on its own line with "5."
insert spaces before 2nd name and add an !, but add sep="" to remove spaces
then print 1st name on its own line, but
insert one less number of spaces before 1st name
"""
print("5.", nametrois)
print("   ", namedeux, "!", sep="")
print("  ", nameun)
print()

"""
print 3rd name with "6." with 3 dashes before it and remove spaces
print 1st name with spaces before it and 6 dashes in front (remove spaces)
print 2nd name with same number of spaces and 9 dashes in fromt (remove spaces)
"""
print("6. ","---", nametrois, sep="")
print("   ", "------", nameun, sep="")
print("   ", "---------", namedeux, sep="")

