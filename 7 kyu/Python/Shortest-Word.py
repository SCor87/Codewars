# DESCRIPTION:

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

#My solution

def find_short(s):
    
    split_string = s.split()
    sorted_string = sorted(split_string, key = len)
    l = len(sorted_string[0])
    
    return l # l: shortest word length