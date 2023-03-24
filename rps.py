import random

print("Welcome to the Rock, Paper, Scissors game!")
name = input("What is your name? ")
print( "Hello " + name + "!")
#list of choices for the computer
my_random_list = ["rock", "paper", "scissors"]
win_count = 0
loss_count = 0
tie_count = 0 

while True:
    
    # get the player's choice
    player_choice = input("Please choose 'rock', 'paper', or 'scissors': (enter 'i quit' to exit)  \n").lower().strip()
    player_choice = " ".join(player_choice.split())
    if player_choice == "i quit":
        break
    
    #get the computer's choice
    computer_choice = random.choice(my_random_list)
    print("\nThe computer chose "+ computer_choice + " and you chose " + player_choice)

    #who is a winner?
    if player_choice == computer_choice:
        print("It's a tie!\n")
        tie_count += 1
        print(f"Your record: | {win_count} Win | {loss_count} Loss | {tie_count} Tie")

    elif ((player_choice == "rock" and computer_choice == "scissors") 
          or (player_choice == "paper" and computer_choice =="rock") 
          or (player_choice == "scissors" and computer_choice == "paper")):
        print("You are a winner! Hurray!\n")
        win_count += 1
        print(f"Your record: | {win_count} Win | {loss_count} Loss | {tie_count} Tie")
    elif player_choice == "i quit":
        break
    else:
        print("You lost. Better luck next time!\n")
        loss_count += 1
        print(f"Your record: | {win_count} Win | {loss_count} Loss | {tie_count} Tie")

print("\nThank you for playing!")






    

