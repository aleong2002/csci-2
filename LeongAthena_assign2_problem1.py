"""
Problem #1: Compound Interest
Athena Leong
Section 04 2/3/22
"""
#overall headers
print("**************************************************")
print(format("3 Year Bank Account Balance Forecast", "^50s"))
print("**************************************************")
print()
print("This program will project how much you could earn by investing money in")
print("a bank account that pays out interest on a yearly basis.")
print()

# 1st year
initinvest = float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
expected1 = int(input("Next, enter the expected interest rate for year 1. For example, enter 5 for 5%: "))
tax1 = float(input("Finally, enter the tax rate on any interest earned this year. For example, enter 15.5 for 15.5%: "))
print()

# 2nd year
year2inv = float(input("How much will you invest at the beginning of year 2? "))
expected2 = int(input("What is the expected interest rate for year 2? "))
tax2 = float(input("What is the expected tax rate for interest earned in year 2? "))
print()

# 3rd year
year3inv = float(input("How much will you invest at the beginning of year 3? "))
expected3 = int(input("What is the expected interest rate for year 3? "))
tax3 = float(input("What is the expected tax rate for interest earned in year 3? "))
print()

# calc interest earned year 1
intearned1 = initinvest * (expected1 / 100)

# calc tax on interest yr 1
inttax1 = intearned1 * (tax1 / 100)

# calc ending earnings yr 1
ending1 = initinvest + (intearned1 - inttax1)

#calc interest earned, tax on interest, and ending earnings yr 2
intearned2 = (ending1 + year2inv) * (expected2 / 100)
inttax2 = intearned2 * (tax2 / 100)
ending2 =  ending1 + year2inv + intearned2 - inttax2

# calc interest earned, tax on interest, and ending earnings yr 3
intearned3 = (ending2 + year3inv) * (expected3 / 100)
inttax3 = intearned3 * (tax3 / 100)
ending3 = ending2 + year3inv + intearned3 - inttax3

# new header
print("--- YOUR FORECAST ---")
print()

# spreadsheet with formatted columns

print(f"{'Year':<10s} {'Starting Balance':>20s} {'Deposit':>15s} {'Interest Earned': >20s} {'Tax on Interest':>20s} {'Ending Balance':>20s}")
print(f"{1: <10d} {0.00: >20.2f} {initinvest: >15,.2f} {intearned1: >20,.2f} {inttax1: >20,.2f} {ending1: >20,.2f}")
print(f"{2: <10d} {ending1: >20,.2f} {year2inv: >15,.2f} {intearned2: >20,.2f} {inttax2: >20,.2f} {ending2: >20,.2f}")
print(f"{3: <10d} {ending2: >20,.2f} {year3inv: >15,.2f} {intearned3: >20,.2f} {inttax3: >20,.2f} {ending3: >20,.2f}")
print()

# total deposited
totaldep = initinvest + year2inv + year3inv
print(f"{'Total deposited:': <30s} ${totaldep: <10,.2f}", sep="")

#total interest earned
totalint = intearned1 + intearned2 + intearned3
print(f"{'Total interest earned:': <30s} ${totalint: <10,.2f}", sep = "")

#total taxes due
totaltax = inttax1 + inttax2 + inttax3
print(f"{'Total taxes due:': <30s} ${totaltax: <10,.2f}", sep="")

"""
formatting examples:
print(format("Year", "<10s"), format("starting", "<20s"), format("Ending", "<15s"))

with f-string formatting (s --> string, d --> int, f --> float):
print(f"{1:<10f} {1000.0: <20,.2f} {2000.0: <15,.2f})
print(2, 3000.0, 4000.0)
"""
