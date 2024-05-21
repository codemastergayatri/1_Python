"""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

d=√((x2 – x1)² + (y2 – y1)²)
"""

##########################################################################################################################
from math import sqrt

def cal_dist(value):
    dist = sqrt(((value[0] - 0)**2 + (value[1] - 0)**2))
    return round(dist)

def distance_calculator(value_distance):
    distance = 0
    start_position = [0,0]
    val2 = value_distance.strip().split('\n')
    # print(val2)
    
    for val in val2:
        list1 = val.split(' ')
        # print(list1)
        if list1[0].upper() in ('UP'):
            start_position[1] = start_position[1] + int(list1[1])
        elif list1[0].upper() in ('DOWN'):
            start_position[1] = start_position[1] - int(list1[1])
        elif list1[0].upper() in ('LEFT'):
            start_position[0] = start_position[0] - int(list1[1])
        elif list1[0].upper() in ('RIGHT'):
            start_position[0] = start_position[0] + int(list1[1])

    # print(start_position)
    print('Distance is: ',cal_dist(start_position))

if __name__ == '__main__':
    user = ''
    user_input = ''
    while user_input != '0':
        user = user + '\n' + user_input
        user_input = input("Enter direction and distance: ")
    distance_calculator(user)
