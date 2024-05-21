"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

##########################################################################################################################

def gen_dict(num):
    dict1 = {}
    list1 = [a for a in range(1,num+1)]
    list2 = [a*a for a in range(1,num+1)]
    # print(list1)
    # print(list2)
    for i in range(len(list1)):
        dict1[list1[i]] = list2[i]
    print(dict1)

if __name__ == '__main__':
    gen_dict(int(input("enter number: ")))