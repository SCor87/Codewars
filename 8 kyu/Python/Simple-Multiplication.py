# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# My solution

def simple_multiplication(number):
    number = 2
    modulus = number % 2

    if modulus == 0:
        new_num = number * 8
    else:
        new_num = number * 9
    print(new_num) 

# OR COMPLETE AS BELOW
# print(number * 8 if number % 2 == 0 else number * 9)