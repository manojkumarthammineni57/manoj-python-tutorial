def greet():
    print("HELLO")
greet()

import sys
print(sys.getrecursionlimit())
def greet():
    print("HELLO")
greet()   

import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
def greet():
    print("HELLO")
greet()

import sys
from time import sleep
sys.setrecursionlimit(100000)
print(sys.getrecursionlimit())
count=1
def greet():
    global count
    print("HELLO",count)
    count=count+1
    sleep(0.02)
    greet()
greet()

    