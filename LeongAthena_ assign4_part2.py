# KAPP_ASSIGNMENT04_PART2
"""
Athena Leong
Problem 2
2/22/2022
"""
import random
print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
print()

# ask for how many wins needed
wins = int(input("How many wins is required to end the tournament? "))

# validate input
# if less than one, continually ask for correct input
while wins < 1:
    print("Invalid, try again")
    wins = int(input("How many wins is required to end the tournament? "))
print()
print("OK, here we go")

# assign accumulator varibales
rounds = 1
numwins = 0
numlosses = 0
numties = 0

# player accumulators
numprock = 0
numpspock = 0
numppaper = 0
numpscissors = 0
numplizard = 0

# computer accumulators
numcrock = 0
numcpaper = 0
numcscissors = 0
numclizard = 0
numcspock = 0

# this loop handles the overall game
# end the game only if user or computer hit the # of wins
while numwins < wins or numlosses < wins:
    print()
    print("-------------------------------------")
    print("Round #" + str(rounds))
    print("You have won", numwins, "rounds")
    print("The computer has won", numlosses, "rounds")
    print("There have been", numties, "ties so far")
    print("-------------------------------------")
    print()
    # get user choice (R, P, S, L or O)
    player = str.upper(input("(R)ock, (P)aper, (S)cissors, (L)izard or Sp(O)ck: "))

    # if the user enters an invalid command you should let them know
    # will loop back to the top and ask for input again
    if player not in ["R", "P", "S", "L", "O"]:
        print("This is an invalid choice, please try again.")
        
    # otherwise command must be good, we can proceed
    else:
        # generate computer's input
        com = random.randint(1, 5)
        # count rounds
        rounds += 1
        # assign computer's moves
        if com == 1:
            complayer = "Rock"
        elif com ==2:
            complayer = "Paper"
        elif com == 3:
            complayer = "Scissors"
        elif com == 4:
            complayer = "Lizard"
        elif com == 5:
            complayer = "Spock"
        print("The computer has selected", complayer)

        # situations
        #Scissors cuts Paper
        if player == "S" and complayer == "Paper":
            print("Scissors cuts Paper!")
            numpscissors += 1
            numcpaper += 1
            win = "yes"
        elif complayer == "Scissors" and player == "P":
            print("Scissors cuts Paper!")
            numcscissors += 1
            numppaper += 1
            win = "no"
        #Paper covers Rock
        elif player == "P" and complayer == "Rock":
            print("Paper covers Rock!")
            numppaper += 1
            numcrock += 1
            win = "yes"
        elif complayer == "Paper" and player == "R":
            print("Paper covers Rock!")
            numcpaper += 1
            numprock += 1
            win = "no"
        #Rock crushes Lizard
        elif player == "R" and complayer == "Lizard":
            print("Rock crushes Lizard!")
            numprock += 1
            numclizard += 1
            win = "yes"
        elif complayer == "Rock" and player == "L":
            print("Rock crushes Lizard!")
            numcrock += 1
            numplizard += 1
            win = "no"
        #Lizard poisons Spock
        elif player == "L" and complayer == "Spock":
            print("Lizard poisons Spock!")
            numplizard += 1
            numcspock += 1
            win = "yes"
        elif complayer == "Lizard" and player == "O":
            print("Lizard poisons Spock!")
            numclizard += 1
            numpspock += 1
            win = "no"
        #Spock smashes Scissors
        elif player == "O" and complayer == "Scissors":
            print("Spock smashes Scissors!")
            numpspock += 1
            numcscissors += 1
            win = "yes"
        elif player == "S" and complayer == "Spock":
            print("Spock smashes Scissors!")
            numpscissors += 1
            numcspock += 1
            win = "no"
        #Scissors decapitates Lizard
        elif player == "S" and complayer == "Lizard":
            print("Scissors decapitates Lizard!")
            #numwins += 1
            numpscissors += 1
            numclizard += 1
            win = "yes"
        elif player == "L" and complayer == "Scissors":
            print("Scissors decapitates Lizard!")
            numplizard += 1
            numcscissors += 1
            win = "no"
        #Lizard eats paper
        elif player == "L" and complayer == "Paper":
            print("Lizard eats Paper!")
            numplizard += 1
            numcpaper += 1
            win = "yes"
        elif player == "P" and complayer == "Lizard":
            print("Lizard eats Paper!")
            numppaper += 1
            numclizard += 1
            win = "no"
        #Paper disproves Spock
        elif player == "P" and complayer == "Spock":
            print("Paper disproves Spock!")
            numppaper += 1
            numcspock += 1
            win = "yes"
        elif player == "O" and complayer == "Paper":
            print("Paper disproves Spock!")
            numpspock += 1
            numcpaper += 1
            win = "no"
        #Spock vaporizes Rock
        elif player == "O" and complayer == "Rock":
            print("Spock vaporizes Rock!")
            numpspock += 1
            numcrock += 1
            win = "yes"
        elif player == "R" and complayer == "Spock":
            print("Spock vaporizes Rock!")
            numprock += 1
            numcspock += 1
            win = "no"
        #Rock crushes Scissors
        elif player == "R" and complayer == "Scissors":
            print("Rock crushes Scissors!")
            numprock += 1
            numcscissors += 1
            win = "yes"
        elif player == "S" and complayer == "Rock":
            print("Rock crushes Scissors!")
            numpscissors += 1
            numcrock += 1
            win = "no"
        # conditions for a tie
        else:
            win = "ties"
            if player == "P":
                numppaper += 1
                numcpaper += 1
            elif player == "R":
                numprock += 1
                numcrock += 1
            elif player == "S":
                numpscissors += 1
                numcscissors += 1
            elif player == "L":
                numplizard += 1
                numclizard += 1
            else:
                numpspock += 1
                numcspock += 1

        # print win lose statements
        if win == "yes":
            print("User wins!")
            numwins += 1
        elif win == "no":
            print("Computer wins!")
            numlosses += 1
        else:
            print("The round has ended in a tie! No points awarded!")
            numties += 1

        # end loop 
        if numwins == wins or numlosses == wins:
            break

# print who wins whole game
if numwins > numlosses:
    print("User wins the game!")
else:
    print("Computer wins the game!")

print()

rocktotal = numprock + numcrock
papertotal = numppaper + numcpaper
scissorstotal = numpscissors + numcscissors
lizardtotal = numplizard + numclizard
spocktotal = numpspock + numcspock

# game summary
print("Game summary:")
print("- Rock was played ", rocktotal, " times (User=", numprock, "; Computer=", numcrock, ")", sep="")
print("- Paper was played ", papertotal, " times (User=", numppaper, "; Computer=", numcpaper, ")", sep="")
print("- Scissors was played ", scissorstotal, " times (User=", numpscissors, "; Computer=", numcscissors, ")", sep="")
print("- Lizard was played ", lizardtotal, " times (User=", numplizard, "; Computer=", numclizard, ")", sep="")
print("- Spock was played ", spocktotal, " times (User=", numpspock, "; Computer=", numcspock, ")", sep="")
