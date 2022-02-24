"""
Problem #0: lottery winnings calculator
Athena Leong
Section 04 2/3/22
"""
# input amount won
winnings = float(input("How much did you win? "))
formwinnings = format(winnings, ",.2f")

# number of people who are splitting
numsplit = int(input("How many people are splitting the winnings? "))
splittotal = float(winnings / numsplit)

#tax rate that will be applied to each person's share
taxrate = int(input("What is the tax rate on lottery winnings (i.e. 25 = 25%) "))
ftaxrate = taxrate / 100
taxperperson = float(splittotal * ftaxrate)

# figure out how much each person earns after taxes are applied
takehome = splittotal - taxperperson

print()

print("In total you won ", "$", format(winnings, ",.2f"), sep="") 
print("Split ", numsplit, " ways that amounts to $", format(splittotal, ",.2f"), " per person", sep="")
print("Tax per person: $", format(taxperperson, ",.2f"), sep="")
print("Take home amount per person: $", format(takehome, ",.2f"), sep="")
