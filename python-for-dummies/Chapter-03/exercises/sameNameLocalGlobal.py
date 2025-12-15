def spam():
    global eggs # declares eggs as a global variable
    eggs = "spam" # assigns "spam" to the global eggs

def bacon():
    eggs = "bacon" # local variable eggs in bacon

def ham():
    print(eggs) # prints the global eggs


eggs = 42 # global variable eggs
spam()
print(eggs)