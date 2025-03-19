def pyramid(x):
    
    for i in range(1, x+1):
    
        for i in range(1, i+1):
            print("*" , end ='')
            
        print("")    
     
x = int(input())

pyramid(x)

#=============================================================================================


def pyramid(x):
    for i in range(1, x + 1):
        for i in range(1, i + 1):
            print(chr(96+i), end="")

        print("")


x = int(input())

pyramid(x)
#=============================================================================================

def pyramid(x):
    
    a = 65
    for i in range(1, x + 1):
     #   spaces = " " * (x - i)
        stars = "*" * (i )
        print(stars)
        a += 1

x = int(input())

pyramid(x)

#=============================================================================================


def pyramid(x):
    
    a = 65
    for i in range(1, x + 1):
     #   spaces = " " * (x - i)
        stars = "%c" %(a) * (i )
        print(stars)
        a += 1

x = int(input())

pyramid(x)

#=============================================================================================

def pyramid(x):
    
    a = 65
    for i in range(1, x + 1):
     #   spaces = " " * (x - i)
        stars = "%c" %(a) * (i -1)
        print(stars)
        a += 1

x = int(input())

pyramid(x)

#=============================================================================================

def pyramid(x):
    
    a = 65
    for i in range(1, x + 1):
        spaces = " " * (x - i)
        stars = "%c" %(a) * (2 * i -1)
        print(spaces + stars)
        a += 1

x = int(input())

pyramid(x)

#=============================================================================================


def pyramid(x):
    
    
    for i in range(1, x + 1):
        spaces = " " * (x - i)
        stars = "*" * (2 * i -1)
        print(spaces + stars)


x = int(input())

pyramid(x)


