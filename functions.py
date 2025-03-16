def Add(a, b) -> int:  # Define a function Add that takes two arguments a and b and returns their sum
    return a + b  # Return the sum of a and b
print(Add(5,6))  # Call the Add function with arguments 5 and 6, and print the result

def Adding(x,y) -> int:  # Define a function Adding that takes two arguments x and y and returns their sum
    d = x + y  # Calculate the sum of x and y, and store it in variable d
    return d  # Return the value of d
x = 10  # Assign the value 10 to variable x
y = 15  # Assign the value 15 to variable y
print(Adding(x,y))  # Call the Adding function with arguments x and y, and print the result

first, second = input().split()  # Take input from the user, split it into two parts, and assign them to variables first and second
print((ord(first) + ord(second)))  # Calculate the sum of the ASCII values of first and second, and print the result

x, y = map(int, input().split())  # Take input from the user, split it into two parts, convert them to integers, and assign them to variables x and y
res = x+y+(x*y)  # Calculate the result of the expression x + y + (x * y), and store it in variable res
if(res == 111):  # Check if the value of res is equal to 111
    print("Yes")  # If res is equal to 111, print "Yes"
else:  # If res is not equal to 111
    print("No")  # Print "No"