"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

##########################################################################################################################

def list_generator(comma_sep1):
    split1 = comma_sep1.split(",")
    return print(split1)
    

def tuple_generator(comma_sep2):
    split2 = comma_sep2.split(",")
    return print(tuple(split2))
    

if __name__ == '__main__':
    user_input = input()
    list_generator(user_input)
    tuple_generator(user_input)