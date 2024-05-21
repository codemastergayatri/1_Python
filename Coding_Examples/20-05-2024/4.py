"""Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
"""

def even_check(num1):
    if num1 % 2 == 0:
        print('It is an even number')
    else:
        print('It is an odd number')

even_check(201)