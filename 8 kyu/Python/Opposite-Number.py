# DESCRIPTION:

# Very simple, given a number (integer / decimal / both depending on 
# the language), find its opposite (additive inverse).

# Examples:

# 1: -1
# 14: -14
# -34: 34

#My solution

def opposite(number):
    
    if number < 0 or number > 0:
        number *= -1
        return number
    else:
        return 0