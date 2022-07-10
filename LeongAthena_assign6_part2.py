"""
Athena Leong
3/22/22
Assignment 6 Part 2
"""
import random
import digitalclock
# data validation
probs = int(input("How many problems would you like to attempt? "))
while probs < 1:
    print("Invalid number, try again")
    probs = int(input("How many problems would you like to attempt? "))
print()

# data validation
while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width < 5:
        print("Invalid width, try again")
    elif width > 10:
        print("Invalid width, try again")
    else:
        break
print()

# data validation
char = input("What character would you like to use? ")
while len(char) > 1:
    print("String too long, try again")
    char = input("What character would you like to use? ")
print()
while True:
    drill = str(input("Would you like to activate 'drill' mode? yes or no? "))
    if drill in ["yes", "no"]:
        break
    else:
        print("Invalid input, try again")
print()
print("Here we go!")
print()

# assign accumulator variables
correct = 0
add = 0
mult = 0
div = 0
sub = 0
addright = 0
subright = 0
multright = 0
divright = 0
addtries = 0
subtries = 0
multtries = 0
divtries = 0
tries = 0


# begin loop
for i in range(probs):
    print("What is .....")
    print()
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    op = random.randint(1, 4)

    digitalclock.print_number(num1, width, char)
    # random operators
    if op == 1:
        operator = "+"
        add +=1
        print(digitalclock.plus(width, char))

    elif op == 2:
        operator = "*"
        mult += 1
        print(digitalclock.multiply(width, char))
        
    elif op == 3:
        operator = "/"
        div += 1
        print(digitalclock.divide(width, char))
        while True:
            if num1 % num2 == 0:
                break
            else:
                num2 = random.randint(1, 9) 
    else:
        operator = "-"
        sub += 1
        print(digitalclock.minus(width, char))

    digitalclock.print_number(num2, width, char)
    ans = int(input("= "))
    check = digitalclock.check_answer(num1, num2, ans, operator)
    # drill mode
    if drill == "yes":
        while check == False:
            tries += 1
            if op == 1:
                addtries += 1
            elif op == 2:
                multtries += 1
            elif op == 3:
                divtries += 1
            else:
                subtries += 1
            print("Sorry, that's not correct.")
            ans = int(input("= "))
            check = digitalclock.check_answer(num1, num2, ans, operator)
        print("Correct!")
    else:
        if check == True:
            print("Correct!")
            correct += 1
            if op == 1:
                addright += 1
            elif op == 2:
                multright += 1
            elif op == 3:
                divright += 1
            else:
                subright += 1
        else:
            print("Sorry, that's not correct")

# ending statements
    print()
if drill == "yes":
    pass
else:
    print("You got", correct, "out of", probs, "correct!")
print()
print("Thanks for playing!")
print()

# calculating percentages
if add == 0:
    pass
else:
    addperc = (addright / add) * 100
  
if sub == 0:
    pass
else:
    subperc = (subright / sub) * 100

if mult == 0:
    pass
else:
    multperc = (multright / mult) * 100
if div == 0:
    pass
else:
    divperc = (divright / div) * 100

# game 
print("---RECORD---")
if add > 0:
    print("Total addition problems presented:", add)
    if drill == "yes":
        if addtries == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", addtries)
    else:
        print(f"Correct addition problems: {addright} ({addperc:.2f}%)")
else:
    print("No addition problems presented")
print()

if sub > 0:
    print("Total subtraction problems presented:", sub)
    if drill == "yes":
        if subtries == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", subtries)
    else:
        print(f"Correct subtraction problems: {subright} ({subperc:.2f}%)")
else:
    print("No subtraction problems presented")
print()

if mult > 0:
    print("Total multiplication problems presented:", mult)
    if drill == "yes":
        if multtries == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", multtries)
    else:
        print(f"Correct multiplication problems: {multright} {multperc:.2f}%)")
else:
    print("No multiplication problems presented")
print()

if div > 0:
    print("Total division problems presented:", div)
    if drill == "yes":
        if divtries == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", divtries)

    else:
        print(f"Correct division problems: {divright} ({divperc:.2f}%)")
else:
    print("No divisions problems presented")
print()
