def spam(divideBy):
    try: # attempts to execute the code that may cause an exception
        return 42 / divideBy
    except ZeroDivisionError: # handles the ZeroDivisionError exception
        return "Error: We do not except zero, Invalid Argument."

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
