# python3
#Matīss Smilga 12. grupa 221RDB131

import sys
import threading
import numpy


def compute_height(n, koks, priekstecis, height, max_height):
    height+=1
    index = int()
    for i in range(0, n):
        if(koks[i] == priekstecis):
            max_height = compute_height(n, koks, i, height, max_height)
            if(height > max_height):
                max_height = height
    return max_height


def main():
    text = input()
    if(text[0] == "I"):
        n = int(input())
        sk = [None] * n
        for i in range(0, n):
            sk[i] = int(input())
    elif(text[0] == "F"):
        text = "test/" + input()
        fails = open(text)
        text = fails.read()
        for index, cip in enumerate(text.split()):
            if(index == 0):
                n = int(cip)
                sk = []
                continue
            sk.append(int(cip))
    
        
    
    garums = int(compute_height(n, sk, -1, 0, 0))
    print(garums)

    
    



    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()

# print(numpy.array([1,2,3]))