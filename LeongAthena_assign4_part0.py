"""
Athena Leong
2/17/2022
Problem 0
"""

num1 = int(input("Number 1: "))

while num1 < 1:
    print("Invalid, try again")
    num1 = int(input("Number 1: "))
""" diff way
while True:
    num2 = int(input("Number 2: "))
    if num2 > num1:
        break
    else:
    print("Invalid")
"""

num2 = int(input("Number 2: "))
while num2 < 1 or num2 <= num1:
    print("Invalid, try again")
    num2 = int(input("Number 2: "))

""" diff way
copy = num1
while num1 < num2:
    print(num1, num1 * "*")
    num1 += 1
while num2 >= copy:
    print(num2, num2 * "*")
    num2 -= 1
"""
star = num1 - 1
while star < num2:
    star += 1
    print(star, " ", "*" * star)

star = num2
while star > num1:
    star -= 1
    print(star, " ", "*" * star)
