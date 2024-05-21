"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

##########################################################################################################################

def calculate_digits_char(value):
    new_value = value.replace(" ", "")
    another_list = [a for a in new_value]
    # print(len(another_list))
    # digit_list = [i for i in another_list if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')] #isdigit()
    # char_list = [i for i in another_list if i in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')] #isalpha
    digit_list = [i for i in another_list if i.isdigit()]
    char_list = [i for i in another_list if i.isalpha()]
    print('LETTERS ',len(char_list))
    print('DIGITS ',len(digit_list))


if __name__ == '__main__':
    user_input = input("Enter a sentence with digits: ")
    calculate_digits_char(user_input)