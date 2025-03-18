"""
Swap two elements 

example: 
Input
x = 3, y = 5
Output
x = 5, y = 3

"""

#=============================================================================================



def swap(x,y):
    
    z = x
    x = y
    y = z
        
    print("X:" ,x)
    print("Y:", y)
    
x = int(input())
y = int(input())
(swap(x,y))

