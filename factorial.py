def factorial(a):
    res = 1
    for i in range (1, a+1):
        
        res = res * i
       
    print(res)        
  
a = int(input())


factorial(a)