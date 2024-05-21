"""Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
"""
def main():
    
    list1 = []
    for i in range(1,21):
        list1.append(i**2)
    tup = tuple(list1)
    print(tup)
    print(*tup,sep=', ')


if __name__ == '__main__':
    main()