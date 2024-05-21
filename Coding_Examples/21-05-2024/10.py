"""With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
"""
def main():
    given_tup = (1,2,3,4,5,6,7,8,9,10)
    lenght = len(given_tup)
    # print(lenght//2)
    print(given_tup[:(lenght//2)])
    print(given_tup[(lenght//2):])

if __name__ == '__main__':
    main()