import random

print("Welcome to the Rock, Paper, Scissors game!")
name = input("What is your name?")
print( "Hello " + name + "!")


#list of choices for the computer
my_random_list = ["rock", "paper", "scissors"]
# get the player's choice
player_choice = input("Please choose rock, paper, or scissors: ").lower()

#get the computer's choice
computer_choice = random.choice(my_random_list)
print("The computer chose "+ computer_choice)

#who is a winner?
if player_choice == computer_choice:
    print("It's a tie!")

elif ((player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice =="rock") or (player_choice == "scissors" and computer_choice == "paper")):
    print("You are a winner! Hurray!")

else:

    print("You lost. Better luck next time!")



    
    
    





    

