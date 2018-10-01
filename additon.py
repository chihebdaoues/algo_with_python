# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 06:14:41 2017

@author: chihebdaoues
"""
L=[2,5,7,15,16,23,42,56,12]
L1=list(range(1,1000,3))
print(L1)
def g(L,s):
    i=0
    j=len(L)-1
    k=1;
    if(s<L[0]):
        print("introuvable: "+str(s))
        return
    while(i<j):
        k+=1        
        if(L[i]+L[j]==s):
            print(i,L[i],j,L[j],s);
            break
        if(L[i]+L[j]<s):
            i+=1
        if(L[i]+L[j]>s):
            j-=1
    print(k)
for i in range(350):
    g(L1,i)