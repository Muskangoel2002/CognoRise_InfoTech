# A Rock-Paper-Scissor game

import random
import os

# User Input

print("\n \t \t Welcome to Rock-Paper-Scissor Game ")
print("Rules:" ,"\n","~ Rock beats Scissor","\n","~Scissor beats Paper","\n","~Paper beats Rock")
print("\nSelect One from : *Rock  *Paper  *Scissor")

x = 0
y = 0

while True:
    user_choice = input("\nYour Choice: ").title()

    # Computer Selection

    Choice = ("Rock","Paper","Scissor")
    Computer_choice = random.choice(Choice)
    print("Computer's Choice is :",Computer_choice)
    print("\n")

    # Game Logic  

    if (user_choice == Computer_choice):
        result =("It's a draw")
    elif (user_choice == "Rock" and Computer_choice == "Scissor"):
        result =("You Won")
    elif (user_choice == "Scissor" and Computer_choice == "Rock"):
        result =("Computer Wins")
    elif (user_choice == "Rock" and Computer_choice == "Paper"):
        result =("Computer Wins")
    elif (user_choice == "Paper" and Computer_choice == "Rock"):
        result =("You Won")
    elif (user_choice == "Paper" and Computer_choice == "Scissor"):
        result =("Computer Wins")
    elif (user_choice == "Scissor" and Computer_choice == "Paper"):
        result =("You Won")
        
    print("\t",result) # Printing result
    
    # Score Tracking
    if (result == "You Won"):
        x += 1
    elif(result == "Computer Wins"):
        y += 1
    else:
        x = x
        y = y

    print("\n Game Score is user vs computer :", x,y) # Printing Score
    
    i=input("\nDo you want to continue the game(yes/no) : ").lower()
    
    if(i == "no"):
        break
    
   
    
