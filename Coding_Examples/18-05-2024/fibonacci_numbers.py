"""example of fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""

def fib(val1, val2):
    value = []
    for i in range(10):
        val1 = val2
        value.append(val1)
        val2 = val1+val2
        value.append(val2)
    print(*value,sep=", ")

if __name__ == '__main__':
    num1 = int(input("enter seed num 1: "))
    num2 = int(input("enter seed num 2: "))
    fib(num1,num2)
    
