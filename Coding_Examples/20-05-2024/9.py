"""Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
"""

def sq():
    list1 = []
    for i in range(1,21):
        list1.append(i**2)
    print(list1)
sq()
