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
