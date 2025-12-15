import random

wins, losses, ties = 0,0,0
selections = ["R", "P", "S"]
random_selection_index = random.randint(0,2)
computer_selection = selections[random_selection_index]



print("ROCK, PAPER, SCISSORS")
print(wins, "wins,", losses, "losses, and", ties, "ties so far.")

while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    user_selection = input().upper()
    if user_selection == "Q":
        print("Thank you for playing, goodbye.")
        break
    elif user_selection not in ["R", "P", "S"]:
        print("Invalid input, please enter r, p, s, or q.")
        continue
    
    if user_selection == "R":
        print("ROCK versus...")
    elif user_selection == "P":
        print("PAPER versus...")
    elif user_selection == "S": 
        print("SCISSORS versus...")

    if computer_selection == "R":
        print("ROCK")
    elif computer_selection == "P":
        print("PAPER")
    elif computer_selection == "S": 
        print("SCISSORS")

    if user_selection == computer_selection:
        print("It's a tie!")
        ties += 1
    elif (user_selection == "R"):
        if computer_selection == "S":
            print("You win! Rock beats Scissors all day!")
            wins += 1
        else:
            print("You lose! Paper beats Rock!")
            losses += 1
    elif (user_selection == "P"):
        if computer_selection == "R":
            print("You win! Paper beats Rock!")
            wins += 1
        else:
            print("You lose! Scissors beat Paper!")
            losses += 1
    elif (user_selection == "S"):
        if computer_selection == "P":
            print("You win! Scissors beat Paper!")
            wins += 1
        else:
            print("You lose! Rock beats Scissors!")
            losses += 1
    print(wins, "wins,", losses, "losses, and", ties, "ties so far.")
    random_selection_index = random.randint(0,2)
    computer_selection = selections[random_selection_index]