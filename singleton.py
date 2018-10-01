# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 23:28:09 2016

@author: chihebdaoues
"""
T = int(input())
l=int(input())
Le=[]
Ls=[]
for i in range(l):
    au, aux = input().strip().split();
    Le.append(int(au));
    Ls.append(int(aux));
s=int(input())
Se=[]
Ss=[]
for i in range(s):
    au, aux = input().strip().split();
    Se.append(int(au));
    Ss.append(int(aux));
for j in range(1,11):
    for i in range(1,11):
        if ((j-1)*10+i) in Le:
            print("Le ",end="");
        elif ((j-1)*10+i) in Ls:
            print("Ls ",end="")
        elif ((j-1)*10+i) in Se:
            print("Se ",end="")
        elif ((j-1)*10+i) in Ss:
            print("Ss ",end="")
        else:
            print('# ',end="")
    print("")