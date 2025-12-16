myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
name = input()

while True:
    if name not in myPets:
        print("I do not know, " + name + ", this is not one of my pets.")
        break
    else:
        print("Of course I know, " + name + ", that is my pet!")
        break