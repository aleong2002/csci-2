"""
Athena Leong
Assignment 8 Part 2
4/08/22
"""
# KAPP_ASSIGNMENT08_PART2
# parallel Pokemon lists
pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
pokemon_fees = [100.00, 50.00, 25.00, 1000.00]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']




# pokemon center loop
while True:
    print("Welcome to the Pokemon Center!")

    # data validation
    command = str.lower(input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: "))
    while command not in ["a", "r", "e", "s", "t", "l", "q"]:
        print("Unknown command, please try again")
        print()
        print("Welcome to the Pokemon Center!")
        command = str.lower(input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: "))
    # set values for adaptive formatting
    namelen = 5
    amountlen = 20
    feelen = 15
    for i in pokemon_names:
        if len(i) > namelen:
            namelen = len(i)
    for i in pokemon_amounts:
        if len(str(i)) > amountlen:
            amountlen = len(str(i))
    for i in pokemon_fees:
        if len(str(i)) > feelen:
            feelen = len(str(i))
    if namelen > 5:
        namelen += 1
    if feelen > 15:
        feelen += 1
    if amountlen > 20:
        amountlen += 1

    # different commands
    if command == "q":
        print("See you next time!")
        break
    # search command
    elif command == "s":
        name = str.lower(input("Name of Pokemon to search for: "))

        if name in pokemon_names:
            location = pokemon_names.index(name)
            print(f"We have {pokemon_amounts[location]} {name.title()} at the Pokemon Center")
            print(f"It will cost ${pokemon_fees[location]:,.2f} to adopt this Pokemon")

            length = len(pokemon_types[location])
            if length > 1:
                print(f"{name.title()} has the following types:", end=" ")

                for x in range(length):
                    
                    print(f'{pokemon_types[location][x].title()}', end=" ")

            else:  
                print(f"{name.title()} has the following types: {pokemon_types[location][0].title()}", end=" ")
            print()            
        
        else:
            print(f"We do not have any {name.title()} at the Pokemon Center")

    # adding a pokemon
    elif command == "a":
        newlist = []
        newp = str.lower(input("Enter name of new pokemon: "))
        if newp in pokemon_names:
            print("Duplicate name, add operation cancelled")
            
        else:
            pokemon_names.append(newp)
            numadd = int(input("How many of these Pokemon are you adding? "))
            while numadd <= 0:
                print("Invalid, please try again")
                numadd = int(input("How many of these Pokemon are you adding? "))
            pokemon_amounts.append(numadd)
    
            afee = float(input("What is the adoption fee for this Pokemon? "))
            while afee <= 0:
                print("Invalid, please try again")
                afee = float(input("What is the adoption fee for this Pokemon? "))
            pokemon_fees.append(afee)

            # to add types
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
            types = 0
            while True:
                poketype = str.lower(input("What type of Pokemon is this? "))
                if types == 0:
                    if poketype == "help":
                        for i in valid_pokemon_types:
                            print("*", i)
                    elif poketype in valid_pokemon_types:
                        if poketype in newlist:
                            print("Duplicate type, please try again")
                        else:
                            print("Type", poketype, "added")
                            types += 1
                            newlist += [poketype]
                    elif poketype == "end":
                        print("You must select at least one Pokemon type")
                    elif poketype not in valid_pokemon_types:
                        print("This is not a valid type, please try again")
                   
                else:
                    if poketype == "help":
                        for i in valid_pokemon_types:
                            print("*", i)
                    elif poketype in valid_pokemon_types:
                        if poketype in newlist:
                            print("Duplicate type, please try again")
                        else:
                            print("Type", poketype, "added")
                            types += 1
                            newlist += [poketype]
                    elif poketype == "end":
                        print("Pokemon Added!")
                        pokemon_types += [newlist]
                        break    
                    elif poketype not in valid_pokemon_types:
                        print("This is not a valid type, please try again")

    # removing a pokemon                    
    elif command == "r":
        rname = str.lower(input("Enter name of Pokemon to remove: "))
        if rname in pokemon_names:
            location = pokemon_names.index(rname)
            del pokemon_names[location]
            del pokemon_amounts[location]
            del pokemon_fees[location]
            del pokemon_types[location]
            print("Pokemon removed")
        else:
            print("Pokemon not found, cannot remove")

    # reporting highest, lowest, and total costs
    elif command == "e":
        # highest prices pokemon
        high = max(pokemon_fees)
        highindex = pokemon_fees.index(high)
        print(f"Highest priced Pokemon: {pokemon_names[highindex].title()} @ ${high:,.2f} per Pokemon")

        # lowest priced pokemon
        low = min(pokemon_fees)
        lowindex = pokemon_fees.index(low)
        print(f"Lowest priced Pokemon: {pokemon_names[lowindex].title()} @ ${low:,.2f} per Pokemon")

        # total cost to adopt all pokemon
        pokesum = 0
        for i in range(0, len(pokemon_names)):
            cost = int(pokemon_amounts[i]) * float(pokemon_fees[i])
            pokesum += cost
        print(f"Total cost to adopt all Pokemon in the Center: ${pokesum:,.2f}")

    # searching by type
    elif command == "t":
        ptype = str.lower(input("Enter Pokemon type: "))
        iteration = 0
        for i in pokemon_types:
            if ptype in i:
                iteration += 1
                if iteration == 1:
                    print(f"{'Name':<{namelen}s} {'Amount Available':>{amountlen}s} {'Adoption Fee':>{feelen}s} {'Type(s)':<s}")
    
                location = pokemon_types.index(i)
                string = pokemon_names[location]
                strup = string.title()
                length = len(pokemon_types[location])
                if length > 1:
                    print(f"{strup:<{namelen}s} {pokemon_amounts[location]:>{amountlen}d} {pokemon_fees[location]:>{feelen},.2f}", end =" ")
                    for x in range(length):
                        
                        print(f'{pokemon_types[location][x].title()}', end=" ")
                    print()    
                else:
                    print(f"{strup:<{namelen}s} {pokemon_amounts[location]:>{amountlen}d} {pokemon_fees[location]:>{feelen},.2f} {pokemon_types[location][0].title():<s}")
            
        
            else:
                if pokemon_types[-1] == i:
                    print("We have no Pokemon of that type at our Pokemon Center")

    # listing with adaptive formatting
    elif command == "l":

        
        print(f"{'Name':<{namelen}s} {'Amount Available':>{amountlen}s} {'Adoption Fee':>{feelen}s} {'Type(s)':<s}")
        for i in range(0, len(pokemon_names)):
            string = pokemon_names[i]
            strup = string.title()
            length = len(pokemon_types[i])
            # pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]

            if length > 1:

                print(f"{strup:<{namelen}s} {pokemon_amounts[i]:>{amountlen}d} {pokemon_fees[i]:>{feelen},.2f}", end =" ")
                for x in range(length):
                    
                    print(f'{pokemon_types[i][x].title()}', end=" ")
                print()
    
            else:
                print(f"{strup:<{namelen}s} {pokemon_amounts[i]:>{amountlen}d} {pokemon_fees[i]:>{feelen},.2f} {pokemon_types[i][0].title()}")
            
    print()     
