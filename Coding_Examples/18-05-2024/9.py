"""A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

##########################################################################################################################
import re
def pwd_validity(pwd):
    get_valid_pwd = []
    list1 = pwd.split(',')
    # print(list1)
    for p in list1:
        if 6 <= len(p) <= 12:
            # print(p)
            if not re.search("[$#@]",p):
                continue
            if not re.search("[a-z]",p):
                continue
            if not re.search("[0-9]",p):
                continue
            if not re.search("[A-Z]",p):
                continue
            get_valid_pwd.append(p)
        else: continue
    print(*get_valid_pwd,sep=',')

if __name__ == '__main__':
    user_input = input("Enter set of valid passwords: ")
    pwd_validity(user_input)