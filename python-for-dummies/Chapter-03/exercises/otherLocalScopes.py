def spam(): # defines function spam
    eggs = 99 # local variable eggs in spam
    bacon() # calls function bacon
    print(eggs) # prints local variable eggs in spam

def bacon(): # defines function bacon
    ham = 101 # local variable ham in bacon
    eggs = 0 # local variable eggs in bacon

spam() # calls function spam