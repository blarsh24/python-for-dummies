catNames = []

while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + " (or enter nothing to stop):")
    name = input()
    if name == "":
        break
    else:
        catNames.append(name)

print("The names of my cats are: ")
for name in catNames:
    print(" " + name)