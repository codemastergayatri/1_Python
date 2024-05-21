"""
Given a 6 x 6 2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are 16  hourglasses in arr. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be 6 x 6.

Example:
input :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

output : 19
"""

#######################################################################################################################################

def get_sum():
    rows = 4
    cols = 4
    list2 = [[0]*rows]*cols
    list1 = []
    arr_of_6_x_6 = [[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]] 
    sum = 0

    for i in arr_of_6_x_6:
        print(*i,sep=' ',end='\n')

    for i in range(0,4):
        for k in range(0,4):
            # print(arr_of_6_x_6[i][k])
            sum = arr_of_6_x_6[i][k] + arr_of_6_x_6[i][k+1] + arr_of_6_x_6[i][k+2] + arr_of_6_x_6[i+1][k+1] + arr_of_6_x_6[i+2][k] + arr_of_6_x_6[i+2][k+1] + arr_of_6_x_6[i+2][k+2]
            list1.append(sum)
    print("*"*20)

    print('max value: ',max(list1))
    list_1 = [a for a in list1[:4]]
    list_2 = [b for b in list1[4:8]]
    list_3 = [c for c in list1[8:12]]
    list_4 = [d for d in list1[12:16]]

    list_main = [list_1, list_2, list_3, list_4]
    print("*"*20)

    for t in list_main:
        print(*t,sep=' ',end='\n')

if __name__ == '__main__':
    get_sum()
    

