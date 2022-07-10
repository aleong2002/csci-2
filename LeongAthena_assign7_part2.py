"""
Athena Leong
Assignment #7 Part 2
3/31/22
"""
# KAPP_ASSIGNMENT07_PART2
import random
# function:   ascii_shift
# input:      a word to shift (String) and the direction to shift by (String, "up" or "down")
# processing: shifts each uppercase character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the direction value.  for example,
#             if word = "APPLE" and direction = "up" the newly generated word would be:
#
#             BQQMF
#
#             because we added +1 to each character. if we were to call the function with
#             word = "BQQMF" and direction = "down" the newly generated word would be:
#           
#             APPLE
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
#             non-uppercase characters should be ignored.  for example, given the string
#             "APPLE pear peach 123" and direction of "up" the function should return:
#
#             BQQMF pear peach 123
#
#             shifting beyond the end of the range of the uppercase characters should result
#             in the letter cycling around to the other side of the alphabet. for example,
#             encoding "XYZ" up would result in "YZA".  likewise, shifting "ABC" down
#             would result in "ZAB".  
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned.
#
#             in the event that an invalid shift direction is supplied no shift will occur and
#             the original string should be returned.  valid directions are "up" and "down"
#             (case sensitive)
#
# output:     returns the newly generated word
def ascii_shift(word, direction):
    newword = ""
    for c in word:
        if c.isupper():
            if direction == "up":
                if c == "Z":
                    newchar = "A"
                else:
                    newchar = chr(ord(c) + 1)
            elif direction == "down":
                if c =="A":
                    newchar = "Z"
                else:
                    newchar = chr(ord(c) - 1)
            else:
                newchar = c
            newword += newchar
        else:
            newword += c
    return newword


# function:   shift_right
# input:      a word to shift (String)
# processing: shifts all characters in the string to the right. the last character in the string
#             will be shifted to the beginning of the string.  for example:
#
#             apple -> eappl
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def shift_right(word):
    newword = ""
    if word != "":
        last = word[-1]
        first = word[0]
        newword += last
        for c in (word[0:-1]):
            newword += c
        return newword
    else:
        return ""


# function:   shift_left
# input:      a word to shift (String)
# processing: shifts all characters in the string to the left. the first character in the string
#             will be shifted to the end of the string.  for example:
#
#             apple -> pplea
#
#             in the event that an empty string is supplied no shift will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def shift_left(word):
    newword = ""
    if word != "":
        last = word[-1]
        first = word[0]
        for c in (word[1:]):
            newword += c
        newword += first
        return newword
    else:
        return ""

# function:   flip
# input:      a word to flip (String)
# processing: flips the first half of the string with the second half of the string.
#             if the string has an even number of characters this function will work as follows:
#
#             ABCD -> CDAB
#
#             if the string has an odd number of characters this function will work as follows:
#
#             ABCDE -> DECAB
#
#             in the event that an empty string is supplied no flip will occur and an empty 
#             string should be returned
#
# output:     returns the newly generated word
def flip(word):
    if word != "":
        if len(word) % 2 == 0:
            newword = ""
            length = len(word)
            half = int(length /2)
            half1 = word[:half]
            half2 = word[half:]
            newword = half2 + half1
            return newword
        else:
            newword = ""
            half = int(len(word) /2) +1
            index = int(len(word) / 2)
            half1 = word[0:half-1]
            half2 = word[index]
            half3 = word[half:]
            newword = half3 + half2 + half1
            return newword
    else:
        return ""


# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
#             you can always assume that the number of letters supplied is
#             a positive number.
# processing: adds a number of random letters (A-Z) after each letter 
#             in the supplied word. for example, if word="CAT" and num=1 
#             we could generate any of the following:
#             CZAQTR
#             CWARTS
#             CEAETT
# 
#             if word="cat" and num=2 we could generate any of the following:
#             CRTAHFTUI
#             CNNANYTJN
#             CZAAAITYM
#
# output:     returns the newly generated word
def add_letters(word, num):
    if word != "":
        newword = ""
        for c in word:
            newword += c
            for i in range(num):
                alph = random.randint(65, 90)
                char = chr(alph)
                newword += char
            

        return newword
    else:
        return ""



# function:   delete_characters
# input:      a word to analyze (String) and the number of characters to remove (integer)
#             you can always assume that the number of characters to remove will be a postive number.
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#             character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word
def delete_characters(word, num):
    if word != "":
        newword = word[::num + 1]
        return newword
        
    else:
        return ""

# decoder/encoder
while True:
    encoding = str.upper(input("Enter an encoding pattern, 'end' to end: "))
    if encoding == "END":
        break
    else:
        
    
        phrase = str.upper(input("Enter a word to encode/decode: "))
        while phrase.isdigit() == True:
            print("Invalid phrase")
            phrase = str.upper(input("Enter a word to encode/decode: "))
        
        for c in encoding:
            if c in ["A", "X", "F", "U", "D", "L", "R"]:
                if c == "A":
                    phrase = add_letters(phrase, 1)
                    print("* Adding 1 letter between all characters:", phrase)
                elif c == "X":
                    phrase = delete_characters(phrase, 1)
                    print("* Deleting 1 character:", phrase)
                elif c == "F":
                    phrase = flip(phrase)
                    print("* Flipping:", phrase)
                elif c == "U":
                    phrase = ascii_shift(phrase, "up")
                    print("* ASCII shifting up:", phrase)
                elif c == "D":
                    phrase = ascii_shift(phrase, "down")
                    print("* ASCII shifting down:", phrase)
                elif c == "L":
                    phrase = shift_left(phrase)
                    print("* Shifting left:", phrase)
                else:
                    phrase = shift_right(phrase)
                    print("* Shifting right:", phrase)
            else:
                print(f"* '{c}' is an invalid command, ignoring")
        print("Final encoding / decoding:", phrase)
        print()
