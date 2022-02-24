# KAPP_ASSIGNMENT03_PART1
"""
Athena Leong
Section 04 2/10/2022
Problem 1
"""
import random
#ask for input for type
prob = str.upper(input("What type of problem do you want to try?  ADDITION, SUBTRACTION, MULTIPLICATION or RANDOM? "))

#if prob == "ADDITION" or prob == "SUBTRACTION" or prob == "MULTIPLICATION" or prob == "RANDOM":
# validates the input, what doesn't fit will not be allowed to be inputted
if prob in ["ADDITION", "MULTIPLICATION", "SUBTRACTION", "RANDOM"]:
    
# determine operator and set problem variable to be used later
# calc answer to problem
# do the same for other operators
    if prob == "ADDITION":
        print("Selection saved -", prob)
        operator = "+"
        
    elif prob == "SUBTRACTION":
        print("Selection saved -", prob)
        operator = "-"
        
    elif prob == "MULTIPLICATION":
        print("Selection saved -", prob)
        operator = "*"
        
# for the random prob type, use random numbers 1 to 3
# set each numerical value equal to a possible prob type   
    else:
        chance = random.randint(1,3)
        if chance == 1:
            
            operator = "+"
            print("... we selected ADDITION as your random problem type")
            
        elif chance == 2:
            
            operator = "-"
            print("... we selected SUBTRACTION as your random problem type")
            
        else:
            
            operator = "*"
            print("... we selected MULTIPLICATION as your random problem type")
    
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    
    if operator == "+":
        problem = "What is " + str(num1) + " + " + str(num2) + "?"
        ans = num1 + num2
    elif operator == "-":
        problem = "What is " + str(num1) + " - " + str(num2) + "?"
        ans = num1 - num2
    else:
        problem = "What is " + str(num1) + " * " + str(num2) + "?"
        ans = num1 * num2
    print("Operator to use:", operator)
    print()
# begin guess 1, set conditions for if they succeed on the first try
# if incorrect, let them know if the answer is higher or lower than the guess
    print("Guess #1")
    print(problem)
    guess = int(input("What is your answer? "))
    if guess == ans:
        print("You answered correctly on your first try!")
    else:
        print("You did not answer correctly on your first try.")
        if guess < ans:
            print("Your answer was too low. Try a higher number next time.")
        else:
            print("Your answer was too high. Try a lower number next time.")
        print()
# nest the second guess under the else since they didn't get it right
# repeat the same conditions
        print("Guess #2")
        print(problem)
        guess = int(input("What is your answer? "))
        if guess == ans:
            print("You answered correctly on your second try!")
        else:
            print("You did not answer correctly on your second try.")
            if guess < ans:
                print("Your answer was too low. Try a higher number next time.")
            else:
                print("Your answer was too high. Try a lower number next time.")
            print()
    # nest the final guess under the 2nd guess' else since they still didn't get it
    # repeat same conditions except don't print whether or not it's higher or lower
    # since it is the final guess
            print("Guess #3")
            print(problem)
            guess = int(input("What is your answer? "))
            if guess == ans:
                print("You answered correctly on your third try!")
            else:
                print("You did not answer correctly on your third try. The correct answer was ", ans, ".", sep="")

else:
    print("Invalid choice, game will end now.")
