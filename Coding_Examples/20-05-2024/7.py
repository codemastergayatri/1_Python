"""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the values only.
"""

def print_dict():
    dict_val = {}
    for i in range(1,21):
        dict_val[i] = i**2
    for i,j in dict_val.items():
        print(j)

print_dict()