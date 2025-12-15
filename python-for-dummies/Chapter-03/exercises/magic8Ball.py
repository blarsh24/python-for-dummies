import random

# List of possible Magic 8-Ball responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Yes – definitely.",
    "Maybe?",
    "Ask later.",
    "Do not count on it.",
    "Yes, or no?",
    "Go away.",
]

while True:
    user_input = input("Ask the Magic 8-Ball something: ") # prompts the user for input
    eight_ball_roll = random.randint(0, 7) # generates a random number between 0 and 7
    print("The Magic 8-Ball says: " + responses[eight_ball_roll]) # prints the response based on the random number
    continue