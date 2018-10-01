# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 00:35:43 2016

@author: chihebdaoues
"""
import pylab as plt;
steps = [];
step=0;
sample = [];
def fastCoinChange(n,mem={}):
    #print(mem);
    global step;
    step+=1;
    if (n==0):
        return [];
    elif( n in mem):
        return mem[n]
    else:
        old = n+1;
        sac=[];
        for i in range(1,n//2+1):
            coin = fastCoinChange(i,mem);
            coins =fastCoinChange(n-i,mem);
            if(len(coin)+len(coins)<old):
                old=len(coin)+len(coins)
                sac = coin+coins;
        mem[n]=sac;
        return mem[n];
for i in range(1,100):    
    print(i,fastCoinChange(i,mem = {1:[1],4:[4],15:[15],20:[20]} ),step );
    steps.append(step)
    step=0
    sample.append(i)
plt.figure("lin");
plt.xlim(0,sample[-1])
plt.plot(sample,steps)
def coinChange(n,mem={}):
    #print(mem);
    global step;
    step+=1
    if (n==0):
        return [];
    elif( n in mem):
        return mem[n]
    else:
        old = n+1;
        sac=[];
        for i in range(1,n//2+1):
            coin = coinChange(i,mem);
            coins =coinChange(n-i,mem);
            if(len(coin)+len(coins)<old):
                old=len(coin)+len(coins)
                sac = coin+coins;
        return sac;
steps=[]
sample=[]
print("not fast coin change");
for i in range(1,25):
    print(i,coinChange(i,mem = {1:[1],4:[4],15:[15],20:[20]} ),step );
    steps.append(step)
    step=0
    sample.append(i)
plt.figure("lin");
plt.ylim(0,steps[-1]+10)
plt.plot(sample,steps)        
        
        
        
        
