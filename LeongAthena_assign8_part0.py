"""
Athena Leong
Assignment 8 Warm-up
"""
import random

sales = []
for i in range(1, 8):
    sale = input(f"Sales for day {i}: ")
    while sale.isdigit() == False:
        print("Sorry, that is not a valid number. Try again.")
        sale = input(f"Sales for day {i}: ")
    while int(sale) < 0:
        print("Sorry, that is not a valid number. Try again.")
        sale = input(f"Sales for day {i}: ")
    sales += [int(sale)]
print()
print("Total sales:", sum(sales))
print(f"Average sales per day: {sum(sales) / len(sales):.2f}")
location = sales.index(max(sales)) + 1
print(f"Highest sales day: {max(sales)} (day {location})")
location = sales.index(min(sales)) + 1
print(f"Highest sales day: {min(sales)} (day {location})")
