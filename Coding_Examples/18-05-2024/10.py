"""You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

##########################################################################################################################
get_list = []

def make_list(value):
    list1 = value.strip().split("\n")
    for i in list1:
        list2 = i.split(",")
        # print(list2)
        get_list.append(tuple(list2))
    get_list.sort()
    print(get_list)

if __name__ == '__main__':
    user = ""
    user_input = ""
    while user_input != '0':
        user = user + '\n' + user_input
        user_input = input("Enter the (name, age, height): ")

    make_list(user)