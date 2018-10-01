from collections import deque
nbrVoleur, sizeVoleur = map(int,input().strip().split())
obj = {}
limit = nbrVoleur*sizeVoleur
Dynam = {}
#print(limit)
ch = input()
while( ch != 'END'):
    row = ch.strip().split(',')
    obj[row[0]] = list(map(int,row[1:]))
    ch = input();
#print(obj)

def calculSac(sac):
    global obj;
    global Dynam;
    Tsac = tuple(sac)
    if Tsac in Dynam.keys():
        return Dynam[Tsac];
    value = 0;
    weight = 0;
    for i in sac:
        value += obj[i][1]
        weight += obj[i][0]
    #print(sac,weight,value)
    Dynam[Tsac] = (weight, value)
    return (weight, value)
items = list(obj.keys())
sac = deque()
for i in items:
    sac.append([i,])
#sac = deque(sac)
#print(sac)
#print(items)
pass
for i in range(10000000):
    curr = sac.popleft();
    #print(curr)
    for j in items:
        aux = curr[:]
        aux.append(j)
        aux.sort()
        if(calculSac(aux)[0] <= limit):
            sac.append(aux)
#print(sac)
chosen = []
Val = 0
while(sac):
    curr = sac.popleft()
    weight, value = calculSac(curr)
    if(weight <=  limit and value > Val):
        Val = value
        chosen = curr[:]
#print(limit)
print(chosen, calculSac(chosen))
print(Dynam)
