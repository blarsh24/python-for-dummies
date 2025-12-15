import random #imports random module

wins, losses, ties = 0,0,0 #initializes win/loss/tie counters
selections = ["R", "P", "S"] #list of possible selections
random_selection_index = random.randint(0,2) #generates random index for computer selection
computer_selection = selections[random_selection_index] #computer's initial selection

# Game introduction
print("ROCK, PAPER, SCISSORS")
print(wins, "wins,", losses, "losses, and", ties, "ties so far.")

# Main game loop
while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit") #prompts user for input
    user_selection = input().upper() #gets user input and converts to uppercase
    if user_selection == "Q": # checks if user wants to quit
        print("Thank you for playing, goodbye.")
        break
    elif user_selection not in ["R", "P", "S"]: #validates user input
        print("Invalid input, please enter r, p, s, or q.")
        continue
    
    # Displays both selections
    if user_selection == "R":
        print("ROCK versus...")
    elif user_selection == "P":
        print("PAPER versus...")
    elif user_selection == "S": 
        print("SCISSORS versus...")

    # Displays computer's selection
    if computer_selection == "R":
        print("ROCK")
    elif computer_selection == "P":
        print("PAPER")
    elif computer_selection == "S": 
        print("SCISSORS")

    # Determines the outcome of the game
    if user_selection == computer_selection: # tie condition
        print("It's a tie!")
        ties += 1
    elif (user_selection == "R"): # Rock
        if computer_selection == "S": 
            print("You win! Rock beats Scissors all day!")
            wins += 1
        else:
            print("You lose! Paper beats Rock!")
            losses += 1
    elif (user_selection == "P"): # Paper
        if computer_selection == "R":
            print("You win! Paper beats Rock!")
            wins += 1
        else:
            print("You lose! Scissors beat Paper!")
            losses += 1
    elif (user_selection == "S"): # Scissors
        if computer_selection == "P":
            print("You win! Scissors beat Paper!")
            wins += 1
        else:
            print("You lose! Rock beats Scissors!")
            losses += 1
    print(wins, "wins,", losses, "losses, and", ties, "ties so far.") # displays current score
    random_selection_index = random.randint(0,2) # generates new random index for computer selection
    computer_selection = selections[random_selection_index] # updates computer's selection