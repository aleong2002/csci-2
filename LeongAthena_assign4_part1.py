# KAPP_ASSIGNMENT04_PART1
"""
Athena Leong
2/22/2022
Program 1
"""
import random

# ask for sides input
sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))

# validate input, has to be one of the given sides
while sides not in [4, 6, 8, 10, 12, 20]:
    print("Invalid size, try again.")
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
print()
print("Thanks, here we go!")
print()

# assign accumulator variables
rolls = 0
die1 = 0
die2 = 0
numhigh = 0
numhighlow = 0
numeven = 0
numodd = 0
nummixed = 0
numsumvalue = 0
numneighbor = 0
nummiddle = 0
numdouble = 0
numsnake = 0
newdie1 = 0
newdie2 = 0

# this loop has the game
while True:
    # generate random die rolls
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    rolls += 1
    newdie1 += die1
    newdie2 += die2

    # game conditions and labels
    # snake eyes
    if die1 == 1 and die2 ==1:
        label = "Odd! Doubles! Snake Eyes!"
        numsnake += 1
        numdouble += 1
        numodd += 1
    # high
    elif die1 == sides and die2 == sides:
        label = "High! Even! Doubles! "
        numhigh += 1
        numeven += 1
        numdouble += 1
    # high / low
    elif (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides):
        label = "High / Low! Mixed!"
        numhighlow += 1
        nummixed += 1
    # even
    elif die1 % 2 == 0 and die2 % 2 == 0:
        if die1 == die2:
            label = "Even! Doubles! "
            numeven += 1
            numdouble += 1
        elif die1 + die2 == sides:
            if die1 == die2:
                label = "Sum Value! Even! Doubles!"
                numsumvalue += 1
                numeven += 1
                numdouble += 1
            else:
                label = "Even! Sum Value!"
                numsumvalue += 1
                numeven += 1
        else:
            label = "Even!"
            numeven += 1
    # odd
    elif die1 % 2 != 0 and die2 % 2 != 0:
        if die1 == die2 and die1 + die2 == sides:
            label = "Odd! Sum Value! Doubles! "
            numodd += 1
            numsumvalue += 1
            numdouble += 1
        elif die1 == die2:
            label = "Odd! Doubles! "
            numodd += 1
            numdouble += 1
        elif die1 + die2 == sides:
            label = "Odd! Sum Value!"
            numodd += 1
            numsumvalue += 1
        else:
            label = "Odd!"
            numodd += 1
    # mixed & middle
    elif (die1 % 2 == 0 and die2 % 2 != 0) or (die1 % 2 != 0 and die2 % 2 == 0):
        if (die1 == sides / 2 and die2 == (sides / 2) + 1) or (die1 == (sides / 2) + 1 and die2 == sides / 2):
            label = "Mixed! Neighbor! Middle!"
            nummixed += 1
            numneighbor += 1
            nummiddle += 1
        elif die1 - die2 == 1 or die2 - die1 == 1:
            label = "Mixed! Neighbor!"
            nummixed += 1
            numneighbor += 1
        else:
            label = "Mixed!"
            nummixed += 1
    # sum value
    elif die1 + die2 == sides:
        if die1 == die2:
            if die1 % 2 == 0 and die2 % 2 == 0:
                label = "Even! Sum Value! Doubles!"
                numeven += 1
                numsumvalue += 1
                numdouble += 1
            else:
                label = "Odd! Sum Value! Doubles!"
                numodd += 1
                numsumvalue += 1
                numdouble += 1
        else:
            label = "Mixed! Sum Value!"
            numsumvalue += 1
            nummixed += 1
    # neighbor
    elif die1 - die2 == 1 or die2 - die1 == 1:
        label = "Mixed! Neighbor!"
        nummixed += 1
        nummiddle += 1
        numneighbor += 1
    
    else:
        label = ""
    # print each roll result
    print(rolls, ". die roll is ", "*", die1, "*", " and *", die2, "* ", label, sep="")

    # if snake eyes, break the loop
    if numsnake == 1:
        break
# calculate percentage and averages   
highperc = (numhigh / rolls) * 100
highlowperc = (numhighlow / rolls) * 100
evenperc = (numeven / rolls) * 100
oddperc = (numodd / rolls) * 100
mixedperc = (nummixed / rolls) * 100
sumperc = (numsumvalue / rolls) * 100
neighborperc = (numneighbor / rolls) * 100
middleperc = (nummiddle / rolls) * 100
doubleperc = (numdouble / rolls) * 100
snakeperc = (numsnake / rolls) * 100
avg1 = (newdie1 / rolls)
avg2 = (newdie2 / rolls)
print()

# orubt on which roll you got snake eyes
# game summary of percentages for each combination and percents
print("You finally got snake eyes on roll #", rolls, sep="")
print(f"Along the way you rolled HIGH {numhigh} time(s). ({highperc:.2f}% of all rolls)")
print(f"Along the way you rolled HIGH / LOW {numhighlow} time(s). ({highlowperc:.2f}% of all rolls)")
print(f"Along the way you rolled EVEN {numeven} time(s). ({evenperc:.2f}% of all rolls)")
print(f"Along the way you rolled ODD {numodd} time(s). ({oddperc:.2f}% of all rolls)")
print(f"Along the way you rolled MIXED {nummixed} time(s). ({mixedperc:.2f}% of all rolls)")
print(f"Along the way you rolled SUM VALUE {numsumvalue} time(s). ({sumperc:.2f}% of all rolls)")
print(f"Along the way you rolled NEIGHBOR {numneighbor} time(s). ({neighborperc:.2f}% of all rolls)")
print(f"Along the way you rolled MIDDLE {nummiddle} time(s). ({middleperc:.2f}% of all rolls)")
print(f"Along the way you rolled DOUBLE {numdouble} time(s). ({doubleperc:.2f}% of all rolls)")
print(f"Along the way you rolled SNAKE EYES {numsnake} time. ({snakeperc:.2f}% of all rolls)")
print(f"Average roll for die #1: {avg1:.2f}")
print(f"Average roll for die #2: {avg2:.2f}")
