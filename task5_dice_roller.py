# a Dice Rolliing Simulator

import random

def roll_dice(sides, rolls):
    print(f"Rolling a {sides}-sided dice {rolls} times:")
    for _ in range(rolls):
        result = random.randint(1, sides)
        print(f"Roll {(_ + 1)}: {result}")

if __name__ == "__main__":
    try:
        sides = int(input("Enter the number of sides on the dice: "))
        rolls = int(input("Enter the number of rolls: "))

        if sides <= 0 or rolls <= 0:
            print("Please enter valid positive integers for sides and rolls.")
        else:
            roll_dice(sides, rolls)
    except ValueError:
        print("Please enter valid integers for sides and rolls.")
