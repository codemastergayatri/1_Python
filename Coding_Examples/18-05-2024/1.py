"""Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting 
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

##########################################################################################################################

def main(value):
    vallist = value.split(" ")
    set_value = set(vallist)
    new_list = list(set_value)
    new_list.sort()
    print(*new_list,sep=" ")

if __name__ == '__main__':
    user_input = str(input("Enter sequence of whitespace separated words: "))
    main(user_input)
