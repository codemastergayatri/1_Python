"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

#IGotInternAtGeeksforgeeks
##########################################################################################################################

def calculate_upper_lower(value):
    list1 = value.replace(" ", "")
    list2 = [a for a in value]
    upper_list = [i for i in list2 if i.isupper()]
    print('UPPER CASE',len(upper_list))
    lower_list = [i for i in list2 if i.islower()]
    print('LOWER CASE',len(lower_list))

if __name__ == '__main__':
    user_input = input("Enter sequence of sentences: ")
    calculate_upper_lower(user_input)