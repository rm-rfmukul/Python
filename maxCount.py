""""
Q3. Find Maximum of two numbers
Q4. Fin Minimum of two numbers

Note: first solve the above questions with:
a. conditional statements
b. ternary operator
c. python in-built functions
"""

#=============================================================================================

def max_condt(x,y):
    
    if(x>y):
        print("X:",x, "is greater than Y:",y)
    else:
        print("Y:",y, "is greater than X:",x)
    
x = int(input())
y = int(input())
(max_condt(x,y))

#=============================================================================================

def max_ter(x,y):
    
    print("x is greater" if x > y else "y is greater")
   
    
x = int(input())
y = int(input())
(max_ter(x,y))

#=============================================================================================

 
 
def max_fun(x,y):
        res = max(x,y)
        print(res)
    
x = int(input())
y = int(input())


max_fun(x,y)

#=============================================================================================
 
 
def min_fun(x,y):
        res = min(x,y)
        print(res)
    
x = int(input())
y = int(input())


min_fun(x,y)

#=============================================================================================


def max_ter(x,y):
    
    print("x is smaller" if x < y else "y is smaller")
   
    
x = int(input())
y = int(input())
(max_ter(x,y))

#=============================================================================================


def max_condt(x,y):
    
    if(x<y):
        print("X:",x, "is smaller than Y:",y)
    else:
        print("Y:",y, "is smaller than X:",x)
    
x = int(input())
y = int(input())
(max_condt(x,y))
