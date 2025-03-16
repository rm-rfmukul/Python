def add(a,b):
    d = a + b
    return d
def sub(a,b):
    if(a > b):
        d = a - b
    else:
        d = b - a
    return d
def mul(a,b):
    d = a * b
    return d
    
a = int(input())
b = int(input())

print(sub(a,b))
print(mul(a,b))
print(add(a,b))


def odd(a,b):
    if (a<b):
        for i in range (a, b):
            if( i % 2 != 0):
                print(i)
    else:
        print("Invalid Range")
            
            
a = int(input())
b = int(input())

odd(a,b)