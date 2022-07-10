"""
Athena Leong
Assignment 10 Part 0
4/21/22
"""

# phrase to iterate over
phrase = "The lazy dog jumped over the curious cat."

# create an empty dictionary
d = {

    }

# iterate over letters in string
for i in phrase:

    # check if char is a letter
    if i.isalpha():

        # if char is already not in the dictionary
        # add to dictionary
        if i not in d:
            d[i] = 1
        # else increase the count by 1
        else:
            d[i] += 1

print("Report by letter, in ascending order by ASCII value:")

# iterate through sorted dictionary
for key in sorted(d):

    # print character and the count of how many times it is used
    print(key, d[key])
