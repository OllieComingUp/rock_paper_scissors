import random
name = input("What is you're name")
print( "Hello " + name )
choice = input("Would you like to choose rock, paper or scissors?")
print("You choose " + choice)
my_random_list = ["rock", "paper", "scissors"]
print(random.choice(my_random_list))