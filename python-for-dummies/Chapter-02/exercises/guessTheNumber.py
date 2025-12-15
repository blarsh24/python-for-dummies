import random # imports random module

rand_number = random.randint(1,20) # generates a random number between 1 and 20.
user_guesses = 0

print("I am thinking of a number between 1 and 20.")

while True:
    user_number = input()
    try:
        value = int(user_number)
    except ValueError:
        print("Please enter an integer between 1 and 20.")
        continue
    if user_guesses == 0 and value == rand_number:
        print("Good job! You guessed the random number on your first try!")
        print("Fun Fact: There was only a 2.5 percent chance of that happening.")
        break
    else:
        user_guesses += 1
    if value > rand_number:
        print("Your guess is too high.")
    elif value < rand_number:
        print("Your guess is too low.")
    else:
        print("You got it! It took you " + str(user_guesses) + " attempts!")
        break
