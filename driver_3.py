# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:55:54 2017

@author: chihebdaoues
"""
import sys;
from heapq import *
from collections import deque
import resource
import time
size=3
def complet(tab):
    k=0;
    for i in tab:
        if i != k:
            return False;
        k+=1
    return True
def Up(tab):
    for i in range(size**2):
        if tab[i]==0:
            break;
    if(i>size-1):
        tab[i]=tab[i-size]
        tab[i-size]=0
    return tab;
def Down(tab):
    for i in range(size**2):
        if tab[i]==0:
            break;
    if(i<size**2-size):
        tab[i]=tab[i+size]
        tab[i+size]=0
    return tab;
def Right(tab):
    for i in range(size**2):
        if tab[i]==0:
            break;
    if(i%size<size-1):
        tab[i]=tab[i+1]
        tab[i+1]=0
    return tab;
def Left(tab):
    for i in range(size**2):
        if tab[i]==0:
            break;
    if(i%size>0):
        tab[i]=tab[i-1]
        tab[i-1]=0
    return tab;
    
def isThere(tab,l):
    for i in l:
        if tab==i[0]:
            return True;
    return False

def isThereA(tab,l):
    for i in l:
        if tab==i[1]:
            return True;
    return False
    
def bfs(tab):
    queue = deque()
    chemin=[]
    explored = [];
    while(not complet(tab)):
        explored.append(tab)
        T = Up(tab[:])
        if(T not in explored and not isThere(T,queue)):
            queue.append((T,chemin+["Up"]))
        T = Down(tab[:])
        if(T not in explored and not isThere(T,queue)):
            queue.append((T,chemin+["Down"]))
        T = Left(tab[:])
        if(T not in explored and not isThere(T,queue)):
            queue.append((T,chemin+["Left"]))
        T = Right(tab[:])
        if(T not in explored and not isThere(T,queue)):
            queue.append((T,chemin+["Right"]))
        print(queue)            
        nex = queue.popleft()
        tab=nex[0]
        chemin=nex[1]
    print(chemin)
    print(len(queue))
    print(tab)

def dfs(tab,limit=0):
    stack = []
    chemin=[]
    explored = [];
    while(not complet(tab)):
        explored.append(tab)
        T = Right(tab[:])
        if(T not in explored and not isThere(T,stack)):
            if(limit==0):
                stack.append((T,chemin+["Right"]))
            elif (len(chemin)+1)<=limit:
                stack.append((T,chemin+["Right"]))
        T = Left(tab[:])
        if(T not in explored and not isThere(T,stack)):
            if(limit==0):
                stack.append((T,chemin+["Left"]))
            elif (len(chemin)+1)<=limit:
                stack.append((T,chemin+["Left"]))
        T = Down(tab[:])
        if(T not in explored and not isThere(T,stack)):
            if(limit==0):
                stack.append((T,chemin+["Down"]))
            elif (len(chemin)+1)<=limit:
                stack.append((T,chemin+["Down"]))
        T = Up(tab[:])
        if(T not in explored and not isThere(T,stack)):
            if(limit==0):
                stack.append((T,chemin+["Up"]))
            elif (len(chemin)+1)<=limit:
                stack.append((T,chemin+["Up"]))
        if(not stack): break;
        nex = stack.pop()
        tab=nex[0]
        chemin=nex[1]
    if(limit==0):
        print(chemin)
        print(len(stack))
        print(tab)
    else:
        return (complet(tab),chemin)

def astV(tab):
    total=0
    i=1;
    while(i<9):        
        for j in range(9):
            if(tab[j]==i):
                break
        total+= (abs(i-j)//3) + (abs(i-j)%3)
        i+=1
    return total

def ast(tab,limit=0):
    #handler = open("kids.txt","w");
    #handler.write(str(tab));
    heap = []
    chemin=[]
    explored = [];
    while(not complet(tab)):
        explored.append(tab)
        T = Up(tab[:])
        V=astV(T)        
        if(T not in explored and not isThereA(T,heap)):
            if(limit==0):
                heappush(heap, (V, T,chemin+["Up"]))
            elif (len(chemin)+1)<=limit:
                heappush(heap, (V, T,chemin+["Up"]))
        T = Down(tab[:])
        V=astV(T)
        if(T not in explored and not isThereA(T,heap)):
            if(limit==0):
                heappush(heap, (V, T, chemin+["Down"]))
            elif (len(chemin)+1)<=limit:
                heappush(heap, (V, T, chemin+["Down"]))
        T = Left(tab[:])
        V=astV(T)
        if(T not in explored and not isThereA(T,heap)):
            if(limit==0):
                heappush(heap, (V, T,chemin+["Left"]))
            elif (len(chemin)+1)<=limit:
                heappush(heap, (V, T,chemin+["Left"]))
        T = Right(tab[:])
        V=astV(T)
        if(T not in explored and not isThereA(T,heap)):
            if(limit==0):
                heappush(heap, (V, T,chemin+["Right"]))
            elif (len(chemin)+1)<=limit:
                heappush(heap, (V, T,chemin+["Right"]))
        if(not heap): break
        nex = heappop(heap)
        chemin= nex[2]
        tab = nex[1]
    if(limit==0):
        print(chemin)
        print(len(heap))
        print(tab)
        return(chemin)
    else:
        return (complet(tab),chemin)

def applyChemin(tab,chemin):
    for i in chemin:
        if(i=="Right"):
             Right(tab)
        elif(i=="Left"):
            Left(tab)
        elif(i=="Down"):
            Down(tab)
        else:
            Up(tab)
    return complet(tab)
    
start_time = time.time()
if(sys.argv[1]=="bfs"):
    tab = [int(i) for i in sys.argv[2].strip().split(",")];
    bfs(tab)
    
elif(sys.argv[1]=="dfs"):
    tab = [int(i) for i in sys.argv[2].strip().split(",")];
    limit=1;
    res = dfs(tab,limit)
    while(not res[0]):
        limit+=1;
        res = dfs(tab,limit);
    print(tab,res[1])

elif(sys.argv[1]=="ast"):
    tab = [int(i) for i in sys.argv[2].strip().split(",")];
    print(tab)
    chemin = ast(tab)
    print(applyChemin(tab,chemin));    
    
elif(sys.argv[1]=="ids"):
    tab = [int(i) for i in sys.argv[2].strip().split(",")];
    limit=1;
    res = ast(tab,limit)
    while(not res[0]):
        limit+=1;
        res = ast(tab,limit);
    print(tab,res[1])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
print("--- %s seconds ---" % (time.time() - start_time))
