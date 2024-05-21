"""Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""
def main():
    list1 = []
    for i in range(1,21):
        list1.append(i)
    list2 = filter(lambda x: x%2==0,list1)
    print(list(list2))

if __name__ == '__main__':
    main()