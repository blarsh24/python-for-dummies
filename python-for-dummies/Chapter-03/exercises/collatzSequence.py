# GOAL:
# write a function that generates the Collatz sequence for a given number n
# The Collatz sequence is defined as follows:
# - Start with any positive integer n
# - If n is even, divide it by 2
# - If n is odd, multiply it by 3 and add 1
# - Repeat the process until n becomes 1

user_input = int(input("Enter a positive integer: "))

def collatz(n): # defines the collatz function with parameter n
    print(n)  # prints the current value of n
    if n == 1: # base case: if n is 1,
        return
    elif n % 2 == 0: # if n is even,
        collatz(n // 2)
    else: # if n is odd,
        collatz(3 * n + 1) 
 
if user_input <= 0:
    print("Please enter a positive integer greater than zero.")
else:
    collatz(user_input)

