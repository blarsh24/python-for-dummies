name = input("Enter your name: ")
age = int(input("Enter your age: "))

if name == "Alice":
    print("Welcome back, Alice!")
elif age < 12:
    print("You are not Alice, kiddo.")
else:
    print("You are not Alice, nor a little kid. Scram.")