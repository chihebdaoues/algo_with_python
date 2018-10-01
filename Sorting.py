    # -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 04:22:52 2016

@author: chihebdaoues
"""
import random;
L1 = []
L2 = []
for i in range(100):
    L1.append(int(random.random()*1000))
for i in range(10**4):
    L2.append(int(random.random()*1000))


def selSort(L):
    for i in range(len(L)):
        m = i
        for j in range(i+1,len(L)):
            if(L[j] <L[m]):
                m=j
        if(m!=i):
            aux = L[m]
            L[m]=L[i]
            L[i]=aux
                

def inSort(L):
    for i in range(1,len(L)):
        j=i-1
        e = L[i]
        while(j>=0 and L[j]>e):
            L[j+1]=L[j]
            j-=1
        L[j+1]=e
        
def mergeSort(L):
    pass

def quickSort(L,s,e):
    if (e-s)>1:
        pivot = e-1;
        k=e-2;
        j=s;
        while(k>=j):
            if(L[pivot]<L[k]):
                aux = L[pivot]
                L[pivot] = L[k]
                L[k] = aux
                k-=1
                pivot -=1
            else:
                aux = L[j]
                L[j] = L[k]
                L[k] = aux
                j+=1
        quickSort(L,s,pivot)
        quickSort(L,pivot+1,e)
