def a(): # defines function a
    print("a() starts")
    b()
    d()
    print("a() returns")

def b(): # defines function b
    print("b() starts")
    c()
    print("b() returns")

def c(): # defines function c
    print("c() starts")
    print("c() returns")

def d(): # defines function d
    print("d() starts")
    print("d() returns")

a() # calls function a to start the call stack