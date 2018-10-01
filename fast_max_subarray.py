# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:54:57 2017

@author: chihebdaoues
"""
import math
import random
L1=list(range(50,100))
#random.shuffle(L1)
#L=[]
#for i in range(1,50):
#    L.append(L1[i]-L1[i-1])
#print(L1)
#L=[25, 10, -28, 25, -43, 28, -15, -12, 22, 7, 18, -42, 34, -31, 8, 9, 3, -26, 16, 1, 17, -5, -20, 4, -11, 3, 17, 14, -4, -13, -18, -5, 15, 17, 10, 3, -29, 9, 3, 20, -13, 8, -40, 8, 23, 12, -7, -31, 14]
#L=[9, 3, -6, 11, 6, 5, -31, 43, -8, -28, -8, 43, -26, 11, -30, 39, -30, 38, -19, -24, 9, 29, -11, 4, -34, -3, 19, 27, -22, -14, 17, -18, 17, -8, 25, -20, -10, -6, 28, -13, -21, 38, 3, -4, -10, 6, -18, 13, 16]
#L=[1, -20, -11, 15, -24, 15, 23, 3, -5, -31, 37, -41, 36, -30, 26, -14, 7, 9, -36, -1, 10, 35, -15, -26, 9, 11, -16, 10, 2, -5, 10, -28, 17, 5, -13, 6, 24, -7, 2, -15, 17, -10, -25, 7, 22, 5, 2, -38, 3]
#L=[48, -40, -5, 22, 3, 3, -21, 22, 17, -47, 18, 3, -12, 33, -35, -8, 17, 3, 5, 9, -8, 3, 13, -36, 34, -26, 4, -13, -1, 31, -14, 17, -25, 24, 4, -26, -12, 25, 18, -34, 24, 8, -21, -12, 21, 7, 6, -12, -17]
#print(L)
def max_sub1(L):
    max_start=0;
    max_end=0;
    max_val=0;
    
    som=0
    aux_start=0
    aux_val=0
    
    for i in range(len(L)):
        #print((aux_val,aux_start),(max_start,max_end,max_val),(som,L[i]))
        som+=L[i]
        if (aux_val==0) and (L[i]>0):
            aux_val=L[i]
            aux_start=i
        else:
            aux_val+=L[i]
        if(som>max_val and aux_val<=som):
            max_end=i
            max_val=som
            aux_val=0
        elif(aux_val>som and aux_val>max_val):
            som = aux_val
            max_val=aux_val
            max_start=aux_start
            max_end=i
            aux_val=0
        if(aux_val<0):
            aux_val=0
    return (max_start,max_end,max_val)
def max_sub(A,low,high):
    if(low+1>=high):
        return (low,high,A[low])
    else:
        mid = math.ceil((low+high)/2)        
        #print(mid)        
        (left_low,left_high,sum_left)=max_sub(A,low,mid)
        #print("L:",(left_low,left_high,sum_left))
        (right_low,right_high,sum_right)=max_sub(A,mid,high)
        #print("R:",(right_low,right_high,sum_right))
        (mid_low,mid_high,sum_mid)=max_cross(A,low,mid,high)
        #print("M:",(mid_low,mid_high,sum_mid))
        if sum_left>= sum_mid and sum_left >= sum_right:
            return (left_low,left_high,sum_left)
        elif(sum_right>=sum_mid and sum_right >= sum_left): 
            return (right_low,right_high,sum_right);
        else:    return (mid_low,mid_high,sum_mid)

def max_cross(A,low,mid,high):
    
    aux=0
    sum_left=0
    sum_right=0
    left_low=mid
    right_high=mid+1
    i=mid;
    while(i>=low):
        aux+=A[i]
        if(aux>sum_left):
            sum_left=aux
            left_low=i
        i-=1
    aux=0
    i=mid+1;
    while(i<high):
        aux+=A[i]
        if(aux>sum_right):
            sum_right=aux
            right_high=i+1
        i+=1
    #print((low,mid,high))
    #print(left_low,right_high,sum_left+sum_right)
    return (left_low,right_high,sum_left+sum_right)
for i in range(10000):
    random.shuffle(L1)    
    L=[]
    for i in range(1,50):
        L.append(L1[i]-L1[i-1])
    x=max_sub(L,0,len(L))
    x= (x[0],x[1]-1,x[2])
    y=max_sub1(L)
    if(x[2]!=y[2]):
        print(L)
        print(x,y)        
        break
    elif (x[0]!=y[0] or y[1]!=x[1])and sum(L[x[0]:x[1]+1])!=sum(L[y[0]:y[1]+1]):
        print(L[x[0]:x[1]+1])
        print(L[y[0]:y[1]+1])
        print(x,y)            
        break