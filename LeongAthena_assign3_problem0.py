"""
Problem 0
Athena Leong
Section 04 2/10/22
"""

# ask for inputs - width & length
width1 = int(input("Enter the width for Rectangle #1: "))
length1 = int(input("Enter the length for Rectangle #1: "))
width2 = int(input("Enter the width for Rectangle #2: "))
length2 = int(input("Enter the length for Rectangel #2: "))
print()

# calc areas
area1 = width1 * length1
area2 = width2 * length2
print("Rectangle #1 has an area of", area1)
print("Rectangle #2 has an area of", area2)
# determine if square (width = length)
if width1 == length1:
    print("Rectangle #1 is a square!")
if width2 == length2:
    print("Rectangle #2 is a square!")
    
print()

#comparing areas
if area1 == area2:
    print("Rectangle #1 and Rectangle #2 are the same size")
elif area1 < area2:
    print("Rectangle #2 is larger than Rectangle #1")
else:
    print("Rectangle #1 is larger than Rectangle #2")
