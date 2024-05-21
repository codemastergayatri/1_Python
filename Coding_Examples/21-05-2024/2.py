"""Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). """

def main():
    given_tup = (1,2,3,4,5,6,7,8,9,10)
    list1 = []
    for i in given_tup:
        if i % 2 == 0:
            list1.append(i)
    print(tuple(list1))


if __name__ == '__main__':
    main()