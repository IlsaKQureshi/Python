print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
input("You are at a cross road. Where do you want to go? Type 'left' or 'right' ")

if input() == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if input() == "wait":
        print("Oh no the tiger at you, better luck next time. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one green and one black.")
        if input() == "red":
            print("It's a room full of fire. Game Over.")
        elif input() == "green": 
            print("You found the treasure! You Win!")
        elif input() == "black":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
else:
  print("You chose to go right. You encounter a band of robbers. Game Over.")