"""
Athena Leong
Assignment 10 Part 1B
4/23/2022
"""

valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']


# move dictionary into a file
# already done
"""
try:
    file = open("pokemon.txt","w")
except:
    print("File cannot be opened")
else:
    for i in sorted(pokemon):
        file.write(i)
        file.write(",")
        file.write(str(pokemon[i]['quantity']))
        file.write(",")
        file.write(str(pokemon[i]['fee']))
        file.write(",")
        newtypes = ",".join(pokemon[i]['types'][::])
        file.write(newtypes)
        file.write("\n")
    file.close()
"""

# try block for opening the text file with dictionary
try:
    file = open("pokemon.txt", "r")

except:
    print("File cannot be opened")

else:
    # read the data
    data = file.read()
    data = data.rstrip()
    file.close()

    # parse through data
    lines = data.split("\n")

    # create empty dictionary
    pokemon = {}

    # parse in lines, and create keys and values
    for line in lines:
        splitline = line.split(",")

        for i in splitline:
            if i == splitline[0]:
                name = i
                pokemon[i] = {}
            elif i == splitline[1]:
                quantity = i
                pokemon[name]['quantity'] = int(quantity)
            elif i == splitline[2]:
                fee = i
                pokemon[name]['fee'] = float(fee)

            # if index is 3 or more, add to a list
            elif i == splitline [3]:
                types = i
                pokemon[name]['types'] = [types]
            else:
                types = i
                pokemon[name]['types'] += [types]



# loop through menu selection
while True:
    print("Welcome to the Pokemon Center!")

    command = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ").lower()

    # if command not a valid choice, continue
    if command not in ["a", "r", "e", "s", "t", "l", "q"]:
        print("Unknown command, please try again")
        print()
        continue

    # if command is q, end program
    if command == "q":
        print("See you next time!")
        break

    # if search, print quantity, fee, and its types
    elif command == "s":
        name = input("Name of Pokemon to search for: ").lower()

        if name in sorted(pokemon):
            print(f"We have {pokemon[name]['quantity']} {name.title()} at the Pokemon Center")
            print(f"It will cost ${pokemon[name]['fee']:,.2f} to adopt this Pokemon")
            newtypes = " ".join(pokemon[name]['types'][::])
            print(f"{name.title()} has the following types: {newtypes.title()} ")

        # else print not at the center
        else:
            print("We do not have any", name.title(), "at the Pokemon Center")

    # adding a pokemon
    elif command == "a":
        name = input("Enter name of new pokemon: ").lower()

        # if pokemon already exists, cancel
        if name in sorted(pokemon):
            print("Duplicate name, add operation cancelled")
            print()
            continue

        # if it doesn't exist
        else:

            # loop through adding
            while True:

                # use try block to avoid non-int inputs
                try:
                    count = int(input("How many of these Pokemon are you adding? "))

                except:
                    print("Not a valid integer, try again")

                else:
                    
                    # if count is invalid, loop
                    while count < 1 or count > 100:
                        print("Invalid, please try again")
                        count = int(input("How many of these Pokemon are you adding? "))

                    # create an empty dictionary
                    pokemon[name] = {}
                    pokemon[name]['quantity'] = count

                    # add a fee
                    fee = float(input("What is the adoption fee for this Pokemon? "))

                    # if fee is less than 1, continue the loop
                    while fee < 1:
                        print("Invalid, please try again")
                        fee = float(input("What is the adoption fee for this Pokemon? "))

                    # add fee key and value
                    pokemon[name]['fee'] = fee
                    
                    print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
                    pokemon[name]['types'] = []
                    # look through adding types
                    while True:
                        types = input("What type of Pokemon is this? ").lower()

                        # end 
                        if types == "end":
                            if len(pokemon[name]['types']) == 0:
                                print("You must select at least one Pokemon type")
                                continue
                            else:
                                print("Pokemon Added!")
                                break

                        # loop through valid_pokemon_types
                        elif types == "help":
                            for i in valid_pokemon_types:
                                print("*", i)

                        else:

                            # if not a valid type, ask for input again
                            while types not in valid_pokemon_types:
                                print("This is not a valid type, please try again")
                                types = input("What type of Pokemon is this? ").lower()

                                # end = break
                                if types == "end":
                                    break

                                # loop thorugh types
                                elif types == "help":
                                    for i in valid_pokemon_types:
                                        print("*", i)

                            # if type is already added, print its a duplicate
                            if types in pokemon[name]['types']:
                                print("Duplicate type, please try again")

                            # else, add the type
                            else:
                                pokemon[name]['types'] += [types]
                                print("Type", types, "added")

                    # end = break
                    if types == "end":
                        break

    # remove pokemon      
    elif command == "r":
        name = input("Enter name of Pokemon to remove: ").lower()

        # if pokemon is in dictionary, delete
        if name in sorted(pokemon):
            del pokemon[name]
            print("Pokemon removed")

        # else, ignore
        else:
            print("Pokemon not found, cannot remove")

    # search by type
    elif command == "t":
        
        count = 0

        # loop until inputted type of pokemon is found in dictionary
        while count == 0:
            types = input("Enter Pokemon type: ").lower()

            # if type isn't valid, break
            if types not in valid_pokemon_types:
                print("We have no Pokemon of that type at our Pokemon Center")
                break

            # loop thorugh dictionary and if type exists count up by one and then break
            for i in sorted(pokemon):
                if types in pokemon[i]['types'][::]:
                    count += 1
                    break

            # if no types are found, print they arent at the center
            if count == 0:
                print("There are no", types.title(), "Pokemon at the Pokemon Center")

            # else, print a report of the pokemon with that type
            else:
                print(f"{'Name':<20s} {'Amount Available':>20s} {'Adoption Fee':>20s} {'Type(s)':<s}")

                for i in sorted(pokemon):

                    if types in pokemon[i]['types']:
                        newtypes = " ".join(pokemon[i]['types'][::])
                        print(f"{i.title():<20s} {pokemon[i]['quantity']:>20d} {pokemon[i]['fee']:>20,.2f} {newtypes.title()} ")

    # list   
    elif command == "l":
        print(f"{'Name':<20s} {'Amount Available':>20s} {'Adoption Fee':>20s} {'Type(s)':<s}")

        # loop through dictionary and print summary
        for i in sorted(pokemon):
            newtypes = " ".join(pokemon[i]['types'][::])
            print(f"{i.title():<20s} {pokemon[i]['quantity']:>20d} {pokemon[i]['fee']:>20,.2f} {newtypes.title()}")
    
    # reporting 
    else:
        # set max and min var
        maximum = -1
        pmax = ""
        pmin= ""
        minimum = 10000000000
        total = 0

        # loop and calculate sum, ad determine max and min
        for item in pokemon:
            sums = pokemon[item]['quantity'] * pokemon[item]['fee']
            
            total += sums
            if pokemon[item]['fee'] > maximum:
                maximum = pokemon[item]['fee']
                pmax = item
            if pokemon[item]['fee'] < minimum:
                minimum = pokemon[item]['fee']
                pmin = item

        # print the results     
        print(f"Highest priced Pokemon: {pmax.title()} @ ${maximum:,.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {pmin.title()} @ ${minimum:,.2f} per Pokemon")
        print(f"Total cost to adopt all Pokemon in the Center: ${total:,.2f}")

    print()

# try block to overwrite previous file
# write into file
# then close
try:
    file = open("pokemon.txt", "w")
except:
    print("File cannot be opened")
else:
    for i in sorted(pokemon):
        file.write(i)
        file.write(",")
        file.write(str(pokemon[i]['quantity']))
        file.write(",")
        file.write(str(pokemon[i]['fee']))
        file.write(",")
        newtypes = ",".join(pokemon[i]['types'][::])
        file.write(newtypes)
        file.write("\n")
    file.close()
