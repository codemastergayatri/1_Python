"""Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = filter(lambda x: x%2==0,list1)
    list3 = map(lambda x: x**2,list2)
    print(list(list3))


if __name__ == '__main__':
    main()