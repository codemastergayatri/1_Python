"""Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
"""
def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = filter(lambda x: x % 2 == 0,list1)
    print(list(list2))

if __name__ == '__main__':
    main()