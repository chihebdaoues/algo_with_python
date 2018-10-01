# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:04:37 2016

@author: chihebdaoues
"""
step =0;
def fib(n):
    global step;
    step +=1;
    if n==0:
        return 1;
    elif n==1:
        return 1;
    else:
        return fib(n-1)+fib(n-2)
def Mfib(n,mem):
    global step;
    step +=1;
    if n in mem:
        return mem[n]
    else:
        mem[n]= Mfib(n-1,mem)+Mfib(n-2,mem)
        return mem[n]
print(Mfib(70,{1:1,0:1}),step)
step=0
print(fib(70),step)
step=0;

"""u1=1
u0=1
i=0

while(i<=10):
    aux=u1+u0
    u0=u1
    u1=aux
    i+=1
print(aux,i)"""
