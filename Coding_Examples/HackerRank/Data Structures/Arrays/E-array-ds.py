"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. 
In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .
Reverse an array of integers.
Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
Example
Return .
Function Description
Complete the function reverseArray in the editor below.
reverseArray has the following parameter(s):
int A[n]: the array to reverse
Returns
int[n]: the reversed array
Input Format
The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .

Constraints:
1 <= N <= 10**3
1 <= A[i] <= 10**4 is the ith integer in A
"""
###########################################################################################################################

from array import array

test_list = [6, 4, 8, 9, 10]

print("The original list : " + str(test_list))

res = array("i", test_list[-1::-1])

print("List after conversion to array : " + str(res))
