"""  q1. You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.

Example 1:

Input:
N = 5
Output:
5 10 15 20 25 30 35 40 45 50
Example 2:

Input:
N = 6
Output:
6 12 18 24 30 36 42 48 54 60 """

#=============================================================================================


def table(x):
    
    for i in range(1,11):
       res = x * i 
       print(res)
    
x = int(input())

(table(x))

