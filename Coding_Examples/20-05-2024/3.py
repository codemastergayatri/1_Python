"""Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.
"""

def max_string(val1,val2):
    result1 = len(val1)
    result2 = len(val2)

    if result1 > result2:
        print(result1)

    else:
        print(result2)

max_string('lenght','lenght_of_this_string')
