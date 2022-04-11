import random

user_wins = 0
#initialize variales here that are user vs computer wins 
computer_wins = 0

options = ["rock", "paper", "scissors"] #using a list called options with our three values of rock paper scissors 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() # we make whatever the user types in lowercase with the .lower() function
    if user_input.lower() == "q":
        break # if they quit we stop the program

    if user_input not in options:
        continue # if they didnt quit we check if the user input is not in the options 
                # if they didn't type in anything from the list then we use continue to start the loop again

    random_number = random.randint(0,2) # is they type in something valid then we generate a random number from 0-2 
    #rock =0 paper=1 scissors=2

    computer_pick = options[random_number] #make a variable that equals to computer picks 
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
        

print("You won,", user_wins, "times.")

print("The computer won", computer_wins, "times.")

print("Goodbye!")
