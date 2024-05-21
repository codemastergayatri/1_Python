"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

##########################################################################################################################
from ast import literal_eval
from math import sqrt

def calculate(d_value):
    c = 50
    h = 30
    d_value = d_value.split(",")
    int_d_v = [literal_eval(a) for a in d_value]
    q_value = [sqrt((2*c*i)/h) for i in int_d_v]
    print("q_value: ", q_value)
    

if __name__ == '__main__':
    calculate(input("Enter value of D: "))
