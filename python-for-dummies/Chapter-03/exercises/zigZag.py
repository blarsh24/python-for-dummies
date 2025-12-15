import time,sys
indent = 0 # How many spaces to indent
indent_increasing = True # Whether the indentation is increasing or not

try:
    while True: # main program loop
        print(" " * indent, end="") # print spaces for indent
        print("********") # print stars
        time.sleep(0.1) # pause for 0.1 seconds

        if indent_increasing: # if indentation is increasing
            indent += 1 # increase indent
            if indent == 20:
                indent_increasing = False # switch to decreasing
        else: # if indentation is decreasing
            indent -= 1
            if indent == 0:
                indent_increasing = True # switch to increasing
except KeyboardInterrupt:
    sys.exit() # exit the program on Ctrl-C