# colours = ["red", "blue", "white", "grey", "pink", "purple", "burgundy"]
# list_comp = [a for a in colours if "p" in a]
# print(list_comp)

###############################################################################################

"""You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. 
Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.

Example
x = 1
y = 1
z = 2
n = 3 
All permutations of [i, j, k] are:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]].
Print an array of the elements that do not sum to n = 3.
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1],  [1, 1, 0],  [1, 1, 2]]"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
print("x = ", x)
print("y = ", y)
print("z = ", z)
print("n = ", n)

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)))



