# To create a Simple Calculator

import math

#Taking input from the user.

First = int(input("Enter the first Number:"))
Second = int(input("Enter the Second Number:"))

print("\n","1.Addition(+)", "\n", "2.Subtraction(-)", "\n","3.Multiplication(*)", "\n","4.Division(/)")
operation = int(input("Enter the operation to be performed : "))

# Performing operations of user's choice by if\else condition.

if(operation == 1):
    result = First + Second
elif(operation == 2):
    result = First - Second
elif(operation == 3):
    result = First * Second
elif(operation == 4):
    result = First / Second
else:
    print ("Invalid input")

# Printing the Results

print("\n")
print("the answer is ", result)
    
    
    
