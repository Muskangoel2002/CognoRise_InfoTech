# To Create a Password generator

import random
import os

#Getting size and complexity from the user

size = int(input("Enter the size of desired password : "))
print ("\n", "1.Easy" ,"\n","2.Medium","\n","3.Difficult")
complexity =input("choose the complexity for your password : ")

# defining the keys for the password

lower_case = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
upper_case = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
numbers = ("1","2","3","4","5","6","7","8","9","0")
characters = ("`","~","@","#","$","%","^","&","*",)

# Making different sets for complexity levels

easy_set = (lower_case + upper_case)
medium_set = ( lower_case + upper_case + numbers)
difficult_set = (lower_case + upper_case + numbers + characters)

# Loop for different complexity password
               
pwd = ""
if(complexity == 1):              
    for x in range(size):
        a = random.choice(easy_set)
        pwd += a
elif(complexity == 2):              
    for x in range(size):
        a = random.choice(medium_set)
        pwd += a
elif(complexity == 3):              
    for x in range(size):
        a = random.choice(difficult_set)
        pwd += a
else:
    print ("invalid input")
    
print(pwd)
