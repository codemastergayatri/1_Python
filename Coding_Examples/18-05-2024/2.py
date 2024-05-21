"""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console."""

##########################################################################################################################

def main(binary_nums):
    new_list = []
    binary_num_list = binary_nums.split(',')
    for v in binary_num_list:
        result_1 = (int(v[0]) * 2**(int(v[len(v)-1]))) + (int(v[1]) + 2**(int(v[len(v)-2]))) + (int(v[2]) + 2**(int(v[len(v)-3]))) + (int(v[3]) + 2**(int(v[len(v)-4])))
        if result_1 % 5 == 0:
            new_list.append(result_1)
    print(*new_list,sep=', ')    

if __name__ == '__main__':
    user_input = input("Enter comma separated binary numbers: ")
    main(user_input)

    # 0100 = 0*2**3 + 1*2**2 + 0*2**1 + 0*2**0 = 0+4+0+0 = 4