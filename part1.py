# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
import random;
x = int(input())
s="abcdefghijklmnopqrsuvwxyz123456789"
pas =""
for i in range(x):
    y = random.random()
    #print(y)
    if int(y*1000%10)%2==0:
        pas+=s[int(y*34)].upper();
    else:
        pas+=s[int(y*34)];
print(" ");
print('#-'+pas)

tC = int(input())
for t in range(tC):
    n,k = [int(i) for i in input().split()]
print(k)
print([ (lambda i: i**2)(t) for t in range(10) if t%2==0])
matrix = [[2,2,3],[4,5,6],[7,8,9]]
print(
[   e
    for row in matrix
    for e in row
    if e%2==0
]
);
try:
    a = int(input())
    b = int(input())
    print(a/b)
    raise Exception("please no chichi plz no!!")
except Exception as msg:
    print(msg)
finally:
    print("Enfin")
"""
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    i = 0
    while(i<len(L)):
        if not g(f(L[i])):
            del(L[i])
            i-=1
        i+=1
    if len(L)==0:
        return -1;
    H = L[:]
    H.sort(reverse=True)
    return H[0]
def g(a):
    return False
def f(b):
    return b*2