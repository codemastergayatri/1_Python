"""Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9"""

##########################################################################################################################

def main(value):
    list1 = value.split(',')
    list2 = [i for i in list1 if (int(i) % 2) != 0]
    print(*list2,sep=',')

if __name__ == '__main__':
    user_input = input("Enter sequence of digits: ")
    main(user_input)