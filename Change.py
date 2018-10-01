# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 02:05:55 2016

@author: chihebdaoues
"""
"""
10 4
2 5 3 6
"""
def changeProb(n,p,l,mem={},tup=[],v=False):
    if p in mem and v and mem[p]:
        for i in mem[p]:
            T = sorted(tup+i)
            if T not in mem[n]:
                mem[n].append(T)
    elif(p==0):
        T = sorted(tup)
        if not T in mem[n]:
            mem[n].append(T);
    else:
        for i in l:
            if(p-i not in mem and p-i>=l[0]):
                mem[p-i]=[]
                changeProb(p-i,p-i,l,mem);
                changeProb(n,p-i,l,mem,tup+[i],True);
            elif(p-i>=0):
                changeProb(n,p-i,l,mem,tup+[i],True);
    pass

n,k= input().strip().split()
n,k=(int(n),int(k))
l=[]
for i in input().strip().split():
    l.append(int(i))
l.sort();
mem={}
for i in l:
    mem[i]=[]
    changeProb(i,i,l,mem);
mem[n]=[]
changeProb(n,n,l,mem)
print(mem)
