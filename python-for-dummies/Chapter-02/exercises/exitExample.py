import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print("...exiting now..")
        sys.exit()
    print('You typed ' + response + '.')