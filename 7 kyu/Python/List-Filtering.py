# In this kata you will create a function that takes a list of non-negative integers
# and strings and returns a new list with the strings filtered out.

# l = [1, 2, 'a', 'b'] Example input from test

def filter_list(l):
    filtered = list(filter(lambda x: isinstance(x, int), l))
    return filtered