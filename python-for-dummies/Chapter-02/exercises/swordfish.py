while True:
    print("Who are you?")
    name = input().capitalize()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password?")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")