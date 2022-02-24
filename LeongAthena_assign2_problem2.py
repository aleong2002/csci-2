"""
Problem #2: Number Gymnastics
Athena Leong
Section 04 2/3/22
"""
#ask for 2 3 digit numbers
numb1 = int(input("Enter a 3 digit number between 000 and 999: "))
numb2 = int(input("Enter a 3 digit number between 000 and 999: "))
print()

# isolate ones, tens, and hundreds places
ones1 = numb1 % 10
ones2 = numb2 % 10
print(format("Digits in the 1's places:", "<28s"), ones1, "and", ones2)
tens1 = (numb1 % 100) // 10
tens2 = (numb2 % 100)// 10
print(format("Digits in the 10's places:", "<28s"), tens1, "and", tens2)
hunds1 = numb1 // 100
hunds2 = numb2 // 100
print(format("Digits in the 100's places:", "<28s"), hunds1, "and", hunds2)
print()

print("Graphical representation of your numbers")
print()
# requires column formatting; multiply digit in place by itself - change to string and multiply
print(format("Hundreds", "<15s"), format("Tens", "<10s"), format("Ones", "<10s"))
ghunds1 = hunds1 * str(hunds1)
ghunds2 = hunds2 * str(hunds2)
gtens1 = tens1 * str(tens1)
gtens2 = tens2 * str(tens2)
gones1 = ones1 * str(ones1)
gones2 = ones2 * str(ones2)
print(f"{ghunds1: <15s} {gtens1: <10s} {gones1: <10s}")
print(f"{ghunds2: <15s} {gtens2: <10s} {gones2: <10s}")
print()

#super number headers
print("Computing Your Super Number!")
print()
print("Step #1: Add Each Place Value")
# add the hundreds places together, tens together, and so on
addhunds = hunds1 + hunds2
print(format("- Hundreds:", "<13s"), hunds1, "+", hunds2, "=", addhunds)
addtens = tens1 + tens2
print(format("- Tens:", "<13s"), tens1, "+", tens2, "=", addtens)
addones = ones1 + ones2
print(format("- Ones:", "<13s"), ones1, "+", ones2, "=", addones)
print()

#step 2 - concatenate the sums, convert to strings
print("Step #2: Combine New Values")
strone = str(addones)
strhund = str(addhunds)
strten = str(addtens)
concatenated = strhund + strten + strone
print("-", addhunds, "+", addtens, "+", addones, "=", concatenated)
print()

#step 3 - sum of the digits in the first number
print("Step #3: Compute The Sum of All Digits in First Number")
sum1 = ones1 + tens1 + hunds1
print("-", hunds1, "+", tens1, "+", ones1, "=", sum1)
print()

#step 4 is the same as 3 but with the 2nd digit
print("Step #4: Compute The Sum of All Digits in Second Number")
sum2 = ones2 + tens2 + hunds2
print("-", hunds2, "+", tens2, "+", ones2, "=", sum2)
print()

#step 5 - combine numbers for step3, 2, and 4 respectively with concatenation
print("Step #5: Combine The Numbers In This Order -- Step 3 + Step 2 + Step 4")
supernumber = str(sum1) + concatenated + str(sum2)
print("-", supernumber)

"""
number = 347
# extract the number in ones, tens, and hundreds places
ones = number % 10
tens = number // 10
hundreds = number // 100
"""
