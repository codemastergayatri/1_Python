"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""

##########################################################################################################################

def sorting_func(get_string_of_words):
    words_string = get_string_of_words.split(",")
    words_string.sort()
    # print(words_string)
    for a in words_string:
        print(a,end=",")

if __name__ == '__main__':
    sorting_func(input("Enter the string of words: "))