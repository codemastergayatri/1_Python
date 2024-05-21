"""Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

##########################################################################################################################
def compute_balance(value):
    
    balance = 0
    for i in value:
        val1 = i.split(' ')
        
        list1 = [a for a in i]
        if 'D' in list1:
            balance = balance + int(val1[1])
        elif 'W' in list1:
            balance = balance - int(val1[1])
    print(balance)

if __name__ == '__main__':
    user_input = ''
    user = []
    while user_input!= '0':
         
        user_input = input("Enter values: ")
        if user_input == '0':
            continue
        else:user.append(user_input)
        
    compute_balance(user)