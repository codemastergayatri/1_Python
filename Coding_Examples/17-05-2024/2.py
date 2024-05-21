"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""

##########################################################################################################################

def finddivisibility(x,y):
    for x in range(x,y+1):
        if x % 5 != 0:
            if x % 7 == 0:
                print(x,end=", ")

if __name__ == '__main__':
    finddivisibility(2000,3200)

