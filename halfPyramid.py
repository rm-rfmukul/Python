def pyramid(x):
    
    for i in range(1, x+1):
    
        for i in range(1, i+1):
            print("*" , end ='')
            
        print("")    
     
x = int(input())

pyramid(x)