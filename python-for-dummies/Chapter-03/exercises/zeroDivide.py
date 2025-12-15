def spam(divideBy): # defines function spam with parameter divideBy
    return 42 / divideBy # returns the result of 42 divided by divideBy

print(spam(2)) # prints 21.0
print(spam(12)) # prints 3.5
print(spam(0)) # this will cause a ZeroDivisionError
print(spam(1)) # prints 42.0