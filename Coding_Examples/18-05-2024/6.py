"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""

##########################################################################################################################

def calculate_value(value):
    
    result = 'a+aa+aaa+aaaa'
    result1 = result.replace('a',str(value))
    print(eval(result1))
        
if __name__ == '__main__':
    user_input = int(input("Enter a number: "))
    calculate_value(user_input)