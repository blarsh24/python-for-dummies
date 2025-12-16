import random

messages = [
    "It is certain",
    "It is decidedly so",
    "Yes - definitely",
    "Reply hazy, try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good"
]

print("Welcome to the Magic 8-Ball!")
print("Ask me a yes/no question:")
user_question = input()  # User input is not used in this version
print("User Question: " + user_question)
print("Thinking...")

print(messages[random.randint(0, len(messages) - 1)])

# option 1 
# print(random.choice(messages))

# option 2
# print(messages[random.randint(0, len(messages) - 1]))