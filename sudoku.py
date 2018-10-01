# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:10:12 2017

@author: chihebdaoues
"""
import resource
import time
def printL(L):
    for i in range(9):
        for j in range(9):
            print(L[i][j],end=" ")
        print("\n");
def testLig(L,c):
    W=[1,1,1,1,1,1,1,1,1]
    for i in range(9):
        if L[c][i] ==0:
            continue
        elif W[L[c][i]-1] == 0:            
            #print("hereL",c)
            return (False,False)
        else:
            W[L[c][i]-1]-=1
    r = []
    emp=0
    for i in range(9):
        if(W[i]!=0):
            r.append(i+1);
            emp+=1
    return (True,r,emp)
    
def testCol(L,c):
    W=[1,1,1,1,1,1,1,1,1]
    for i in range(9):
        if L[i][c]==0:
            continue
        elif W[L[i][c]-1] == 0:
            #print("hereC",c)
            return (False,False)
        else:
            W[L[i][c]-1] -=1
    r = []
    emp=0
    for i in range(9):
        if(W[i]!=0):
            r.append(i+1);
            emp+=1
    return (True,r,emp)
    
def testCase(L,c):
    W=[1,1,1,1,1,1,1,1,1]
    for i in range(3):
        for j in range(3):
            if L[(c//3)*3+i][(c%3)*3+j]==0:
                continue
            elif W[L[(c//3)*3+i][(c%3)*3+j]-1] == 0:
                #print("hereCase",c)
                return (False,False)
            else:
                W[L[(c//3)*3+i][(c%3)*3+j]-1] -=1
    r = []
    emp=0;
    for i in range(9):
        if(W[i]!=0):
            r.append(i+1);
            emp+=1
    return (True,r,emp)
def Complet(L):
    emp=0;
    for i in range(3):
        for j in range(3):
            case= testCase(L,i*3+j)
            lig = testLig(L,i*3+j)
            col = testCol(L,i*3+j)
            if not (case[0] and lig[0] and col[0]) :
                return (False,False)
            if case[1]+lig[1]+col[1]:
                emp+=case[2]
    return (True,emp) #(no error,complet)
def addElementCol(L,c,k):
    for i in range(9):
        if L[i][c]==0:
            L[i][c]=k
            break;
def addElementLig(L,c,k):
    for i in range(9):
        if L[c][i] ==0:
            L[c][i]=k
            break;
def addElementCase(L,c,k):
    for i in range(3):
        for j in range(3):
            if L[(c//3)*3+i][(c%3)*3+j]==0:
                L[(c//3)*3+i][(c%3)*3+j]=k;
                break;
def addElementColLig(L,c,l,k):
    if L[l][c]==0:
        L[l][c]=k
def addElementLigCase(L,l,C,k):
    for i in range(3):
        if L[l][(C%3)*3+i]==0:
            L[l][(C%3)*3+i]=k;
            break;
def addElementCaseCol(L,C,c,k):
    for i in range(3):
        if L[(C//3)*3+i][c]==0:
            L[(C//3)*3+i][c]=k;
            break;
def intersect(a, b):
    return list(set(a) & set(b))
def Anti_intersect(a, b):
    S= set(b)
    S2 = set([1,2,3,4,5,6,7,8,9])
    for i in a:
        if i != "#":
            S2&=(set(i) & S) ^ set([1,2,3,4,5,6,7,8,9])
    S&=S2
    return list(S)

def findCases(i,j,L):
    sortie=[]
    for k in range(i-i%3,i-i%3+3):
        for k1 in range(j-j%3,j-j%3+3):
            if((k,k1)==(i,j) or L[i][j]=="#"):
                continue
            sortie.append(L[k][k1])
    return sortie
"""L=[[0,1,7, 4,9,6, 5,3,8],
   [4,9,6, 8,3,5, 7,2,1],
   [5,3,8, 7,2,1, 4,6,9],

   [6,4,2, 0,1,3, 8,7,5],
   [9,8,5, 6,7,2, 3,1,4],
   [1,7,3, 5,4,8, 2,9,6],

   [7,5,9, 2,6,4, 0,8,3],
   [8,2,1, 3,5,9, 6,4,7],
   [3,6,4, 1,8,7, 9,5,2]]

L=[[0,0,0, 0,0,3, 0,0,0],
   [0,1,0, 0,0,0, 6,7,0],
   [0,7,0, 6,4,1, 0,0,0],

   [9,0,2, 3,0,6, 4,0,0],
   [0,0,5, 0,2,0, 3,0,0],
   [0,0,6, 8,0,4, 1,0,2],

   [0,0,0, 1,6,9, 0,4,0],
   [0,2,1, 0,0,0, 0,8,0],
   [0,0,0, 4,0,0, 0,0,0]]

L=[[0,0,0, 0,8,0, 0,0,0],
   [0,8,6, 7,0,0, 5,9,3],
   [0,1,0, 0,0,0, 8,0,0],

   [0,0,2, 0,6,0, 0,0,8],
   [8,0,0, 4,0,0, 7,3,0],
   [0,0,5, 0,9,0, 0,0,2],

   [0,5,0, 0,0,0, 6,0,0],
   [0,3,7, 8,0,0, 1,5,9],
   [0,0,0, 0,7,0, 0,0,0]]
   
L=[[0,0,0, 7,0,0, 9,0,0],
   [0,0,0, 0,4,8, 6,0,0],
   [4,6,0, 0,5,0, 0,0,0],
   
   [0,7,0, 8,0,1, 0,0,5],
   [0,1,3, 0,0,0, 2,7,0],
   [5,0,0, 6,0,2, 0,8,0],
   
   [0,0,0, 0,2,0, 0,3,4],
   [0,0,6, 5,1,0, 0,0,0],
   [0,0,7, 0,0,4, 0,0,0]]

L=[[0,0,0, 0,0,0, 0,3,8],
   [0,3,0, 0,2,0, 0,6,0],
   [0,0,4, 0,3,1, 0,0,0],
    
   [2,0,0, 3,0,0, 8,0,0],
   [3,4,0, 1,0,6, 0,9,2],
   [0,0,8, 0,0,7, 0,0,3],
    
   [0,0,0, 6,1,0, 9,0,0],
   [0,6,0, 0,7,0, 0,1,0],
   [4,8,0, 0,0,0, 0,0,0]]
   
L=[[0,0,6, 0,0,9, 5,0,7],
   [0,5,0, 0,1,0, 0,0,0],
   [3,0,0, 0,5,0, 2,0,0],
   
   [9,0,5, 0,0,0, 0,4,0],
   [0,0,0, 0,3,7, 0,2,0],
   [1,0,2, 0,0,0, 0,8,0],
   
   [4,0,0, 0,6,0, 8,0,0],
   [0,6,0, 0,2,0, 0,0,0],
   [0,0,8, 0,0,1, 4,0,6]]

L=[[0,7,9, 1,0,2, 6,5,0],
   [3,0,0, 0,5,0, 0,0,2],
   [0,0,0, 6,0,8, 0,0,0],
   
   [0,4,3, 0,0,0, 1,2,0],
   [0,0,1, 0,7,0, 3,0,0],
   [2,0,0, 0,0,0, 0,0,7],
   
   [6,0,0, 4,0,5, 0,0,1],
   [0,3,2, 0,6,0, 5,7,0],
   [0,0,5, 0,0,0, 2,0,0]]"""
L=[[1,2,3, 4,5,6, 7,8,9],
   [4,5,6, 0,0,0, 0,0,0],
   [7,8,9, 0,0,0, 0,0,0],
   
   [0,0,0, 0,0,0, 0,0,0],
   [0,0,0, 0,0,0, 0,0,0],
   [0,0,0, 0,0,0, 0,0,0],
   
   [0,0,0, 0,0,0, 0,0,0],
   [0,0,0, 0,0,0, 0,0,0],
   [0,0,0, 0,0,0, 0,0,0]]
#L=[]
#for j in range(9):
#    L.append( [ int(i) for i in input().strip().split(",") ])
start_time = time.time()
End=False
error=False
daguez=[]
ldaguez=0
while(not End):
    #printL(L)
    #print(Complet(L))
    #input()    
    End = True
    Cases = []
    Lignes = []
    Colonnes = []    
    
    for i in range(9):
        O = testCase(L,i);
        if O[0]:
            Cases.append(O)
        else:
            error = True;
            break
        O = testLig(L,i)
        if O[0]:
            Lignes.append(O)
        else:
            error = True;
            break
        O = testCol(L,i)
        if O[0]:
            Colonnes.append(testCol(L,i))
        else:
            error = True;
            break
    if(not error):
        for i in range(9):
            if Cases[i][0] and len(Cases[i][1])==1:
                addElementCase(L,i,Cases[i][1][0])
                End = False
                break
            if Lignes[i][0] and len(Lignes[i][1])==1:
                addElementLig(L,i,Lignes[i][1][0])
                End = False
                break
            if Colonnes[i][0] and len(Colonnes[i][1])==1:
                addElementCol(L,i,Colonnes[i][1][0])
                End = False
                break
        if not End:
            continue
        inter= []
        for i in range(9):
            inter.append([])
            for j in range(9):
                if L[i][j]==0:
                    x=intersect(intersect(Lignes[i][1],Colonnes[j][1]),
                                                 Cases[(i//3)*3+j//3][1])
                    inter[i].append(x)
                    if(len(x)==1):
                        addElementColLig(L,j,i,x[0])
                        End=False
                        break
                else:
                    inter[i].append("#")
            if(not End):
                    break
        if not End:
            continue
        for i in range(9):
            for j in range(9):
                if(inter[i][j]=="#"):
                    continue
                b=inter[i][j]
                Li0 = [inter[i][(j+1)%9],inter[i][(j+2)%9],
                      inter[i][(j+3)%9],inter[i][(j+4)%9],inter[i][(j+5)%9],
                    inter[i][(j+6)%9],inter[i][(j+7)%9],inter[i][(j+8)%9]]
                anti = Anti_intersect(Li0, b)
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                
                Li1=[inter[(i+1)%9][j],inter[(i+2)%9][j],
                      inter[(i+3)%9][j],inter[(i+4)%9][j],
                    inter[(i+5)%9][j],inter[(i+6)%9][j],
                    inter[(i+7)%9][j],inter[(i+8)%9][j]]
                anti = Anti_intersect(Li1, b)
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                
                Li2=findCases(i,j,inter)
                anti = Anti_intersect(Li2, b)
                
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                anti = Anti_intersect(Li0+Li1, b)
                
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                anti = Anti_intersect(Li2+Li1, b)
    
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                anti = Anti_intersect(Li0+Li2, b)
    
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
                anti = Anti_intersect(Li0+Li1+Li2, b)
    
                if len(anti)==1:
                    L[i][j]=anti[0]
                    End=False
                    break
            if not End:
                break
        if not End:
            continue
        Com = Complet(L)
        if(Com[0] and Com[1]!=0):
            minListe=(0,0,10);
            for i in range(9):
                for j in range(9):
                    if(inter[i][j]!="#" and len(inter[i][j])<minListe[2]):
                        minListe=(i,j,len(inter[i][j]));
            for i in inter[minListe[0]][minListe[1]]:
                aux = [i[:] for i in L]
                aux[minListe[0]][minListe[1]]=i
                daguez.append(aux)
                ldaguez+=1
            print(ldaguez)
            L=daguez.pop()
            End=False
    elif len(daguez)!=0:
        L=daguez.pop()
        End=False
        error=False
printL(L)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
print("--- %s seconds ---" % (time.time() - start_time))


