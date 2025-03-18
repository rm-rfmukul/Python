"""
q2. Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

Example:

Input:
x = 3
Output:
3 2 1 0
Explanation:
Numbers in decreasing order from 3
are 3, 2, 1, 0

"""

#=============================================================================================



def decr(x):
    
    for i in reversed(range(x)):
        
       print(i)
    
x = int(input())

(decr(x))

#=============================================================================================



def decr(x):
    
    for i in range(x, -1, -1):
        
       print(i)
    
x = int(input())

(decr(x))

