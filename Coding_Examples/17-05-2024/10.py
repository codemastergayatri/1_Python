"""Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

##########################################################################################################################

def main(val1):
    print(val1.upper())

if __name__ == '__main__':
    user_input = ""
    other_value = ""
    
    while user_input != "0":
        other_value = other_value + "\n " + user_input
        user_input = input("Enter sequence of sentences, press 0 to end: ")       
    main(other_value)