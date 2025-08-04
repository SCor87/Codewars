# In this kata you will create a function that takes a list of non-negative integers
# and strings and returns a new list with the strings filtered out.

l = [1, 2, 'a', 'b']

# def filter_list(l):

only_words = filter(str.isalpha, l)
print(only_words)


# l.remove()
# print(l)

# my_list = ['foo','bar','baz','>=','5.2']

# # With
# only_words = [token for token in my_list if token.isalpha()]

# # Without
# only_words = filter(str.isalpha, my_list)