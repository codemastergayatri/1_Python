"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

##########################################################################################################################

def factorial(num):
    num1 = 1
    for i in range(1,num+1):
        num1 = num1*i
        
    print(num1)

if __name__ == '__main__':
    factorial(int(input("enter num: ")))