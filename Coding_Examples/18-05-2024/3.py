"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line."""

##########################################################################################################################
list1 = []
def main():
    for i in range(1000,3001):
        if i % 2 == 0:
            if "1" not in str(i) and "3" not in str(i) and "5" not in str(i) and "7" not in str(i) and "9" not in str(i) and "0" not in str(i):
                list1.append(i)
    return list1

if __name__ == '__main__':
    print(*main(),sep=',')