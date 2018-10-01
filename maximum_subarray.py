# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:54:40 2017

@author: chihebdaoues
"""
import random
L1=list(range(50,100))
random.shuffle(L1)
L=[]
for i in range(1,50):
    L.append(L1[i]-L1[i-1])
print(L1)
print(L)

def max_sub(A,low,high):
    if(low+1>=high):
        return (low,high,A[low])
    else:

        mid = (low+high)//2
        (left_low,left_high,sum_left)=max_sub(A,low,mid)
        (right_low,right_high,sum_right)=max_sub(A,mid,high)
        (mid_low,mid_high,sum_mid)=max_cross(A,low,mid,high)
        if sum_left> sum_mid and sum_left > sum_right:
            return (left_low,left_high,sum_left)
        elif(sum_right>sum_mid and sum_right > sum_left):
            return (right_low,right_high,sum_right);
        else:    return (mid_low,mid_high,sum_mid)

def max_cross(A,low,mid,high):
    aux=0
    sum_left=0
    sum_right=0
    left_low=0
    right_high=0    
    for i in range(mid-1,low-1,-1):
        aux+=A[i]
        if(aux>sum_left):
            sum_left=aux
            left_low=i
    aux=0
    for i in range(mid,high):
        aux+=A[i]
        if(aux>sum_right):
            sum_right=aux
            right_high=i
    return (left_low,right_high,sum_left+sum_right)
print(max_sub(L,0,len(L)))
