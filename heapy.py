L=[27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
print(L);
def heapify(A,i,heapSize):
    done=True
    while(done):
        done = False
        l=2*i+1
        r=2*i+2
        largest = i
        if l<=heapSize and r<=heapSize:
            print(A[l],"<--",A[i],"-->",A[r]);
        elif r<=heapSize:
            print(A[i],"-->",A[r]);
        elif l<=heapSize:
            print(A[l],"<--",A[i])
                  
        if l<=heapSize and A[l]>A[i]:
            largest = l;
        if r<= heapSize and A[r]>A[largest]:
            largest=r;
        if largest != i :
            aux = A[i]
            A[i] = A[largest]
            A[largest]=aux
            done=True;
            i=largest;
#heapify(L,2);
#print(L)
def heapBuild(A,heapSize):
    i=heapSize/2;
    while (i>= 0):
        heapify(A,i,heapSize)
        i-=1
def heapSort(L):
    i = len(L)-1
    heapBuild(L,i)
    while(i>=1):
        aux = L[i]
        L[i]=L[0]
        L[0]=aux
        i-=1
        heapBuild(L,i);
    pass
heapSort(L)
print(L)
