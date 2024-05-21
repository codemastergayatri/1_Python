"""Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
"""
def main(value):
    if value in ("YES") or value in ("yes") or value in ("Yes"):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    user_input = input("Enter a string: ")
    main(user_input)