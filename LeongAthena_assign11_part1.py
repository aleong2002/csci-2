"""
Athena Leong
Assignment 11 Part 1
4/28/22
"""
# KAPP_ASSIGNMENT11_PART2
import random

class Gumball_Machine:
    # runs when machine is built
    def __init__(self, capacity):
        # how many gumballs can be held in machine
        self.capacity = capacity

        # each machine starts with $0.00
        self.money = 0.00

        # list of types of gumballs
        self.gumballs = []
        for i in range(self.capacity):
            
            gt = random.randint(1, 3)
            if gt == 1:
                self.gumballs.append("red")
            elif gt == 2:
                self.gumballs.append("green")
            else:
                self.gumballs.append("blue")
        print("Gumball Machine created with", self.capacity, "random gumballs")

    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:", len(self.gumballs))
        print(f"* Money in machine: ${self.money:,.2f}")
        
    def dispense(self, coin):
        if coin == 0.25:
            if len(self.gumballs) > 0:
                print("Accepting 0.25; Dispensing a", self.gumballs[0], "gumball")
                self.money += .25
                del self.gumballs[0]
            else:
                print("Machine is empty, no gumball will be dispensed")
        else:
            print("Invalid coin, no gumball will be dispensed")

    def count_gumballs_by_type(self, gtype):
        count = 0
        for i in self.gumballs:
            if i == gtype:
                count += 1

        print("There are", count, "gumballs of type", gtype, "in the gumball machine")

# TESTER CODE

machine = Gumball_Machine(5)
print()
machine.report()
print()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
print()
machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)
print()
machine.report()
print()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
print()
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
print()
machine.report()
print()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
print()
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
print()
machine.report()
print()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
