def isPrime(x):
        
        for i in range(2,x):
        
            if(x % i == 0):
                return False 
            
        return True    
            
  
a = int(input())

for i in range (1, a+1):
    
    if((isPrime(i)) == True):
        print(i)
