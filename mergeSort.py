# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:02:45 2017

@author: chihebdaoues
"""
import random
A=list(range(500))
random.shuffle(A)
#L=[0,3,4,6,10]
#R=[1,2,5,7,11]
#merge(A,L,R)
#print(A);
def merge(A,p,r,q):
    L=[]
    R=[]
    for i in range(p,r):
        L.append(A[i])
    for i in range(r,q):
        R.append(A[i])
    i=0
    j=0
    k=p
    while(i<len(L) and j< len(R)):
        if(L[i]>R[j]):
            A[k]=(R[j])
            j+=1
        else:
            A[k]=(L[i])
            i+=1
        k+=1
    while(i<len(L)):
        A[k]=(L[i])
        i+=1
        k+=1
    while(j<len(R)):
        A[k]=(R[j])
        j+=1
        k+=1
    print(A)
def merge_sort(A,p,q):
    if(q-p>1):
        r=(p+q)//2
        merge_sort(A,p,r)
        merge_sort(A,r,q)
        merge(A,p,r,q)
merge_sort(A,0,len(A))
