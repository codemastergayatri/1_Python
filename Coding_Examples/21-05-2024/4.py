"""Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""
def main():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    squaredNumbers = map(lambda x: x**2, list1)
    print(list(squaredNumbers))


if __name__ == '__main__':
    main()