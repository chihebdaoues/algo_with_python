def showRide(R):
    for i in R:
        print(i.id,i.sPosition,i.fPosition,i.es,i.lf,i.cost)

def showCars(C):
    for i in C:
        #print("The Car: ",i.id,i.position,i.usedSteps)
        #print("Ride:")
        #showRide(i.Rides)
        print(len(i.Rides),end=" ")
        for j in i.Rides:
            print(j.id,end=" ")
        print("")
def showCar(i):
    print("The Car: ",i.id,i.position,i.usedSteps)
    print("Ride:")
    showRide(i.Rides)
    
def calcValue(R,C,B):
    stepToRide = abs(C.position[0]-R.sPosition[0]) + abs(C.position[1]-R.sPosition[1]) 
    stepMade = stepToRide + C.usedSteps
    value=0;
    if(stepMade < R.es):
        value = B * (R.es-stepMade)
    elif(stepMade + R.cost > R.lf):
        return -1;
    value += R.cost
    return value

class Ride(object):
    def __init__(self,idd,sx, sy, fx, fy, es, lf):
        self.id = idd
        self.sPosition = (sx,sy)
        self.fPosition =(fx,fy)
        self.es = es
        self.lf = lf
        self.cost = abs(sx-fx)+abs(fy-sy)

class car:
    def __init__(self,idd):
        self.Rides = []
        self.id = idd
        self.position = (0,0)
        self.usedSteps = 0;
    def addRide(self,R):
        self.Rides.append(R);
        self.usedSteps += R.cost +  abs(self.position[0]-R.sPosition[0]) + abs(self.position[1]-R.sPosition[1])
        self.position = R.fPosition
        
def assignRideCar(Cars,Rides,Bonus,ACars):
    auxRide = 0
    auxCar = 0
    auxValue=0
    toDel = []
    for i in ACars:
        delCar = True
        for j in range(len(Rides)):
            aux = calcValue(Rides[j],Cars[i],Bonus)
            #print("Value:",aux,"if Ride:",j,'and Car:',i)
            if(auxValue < aux):
                delCar = False
                auxValue = aux
                auxCar = i
                auxRide = j
        if(delCar):
            toDel.append(i)
    for i in toDel:
        ACars.remove(i)
    #print("Officiel Value:",auxValue,"Ride:",auxCar,'and Car:',auxRide)
    Cars[auxCar].addRide(Rides[auxRide])
    #showCar(Cars[auxCar])
    del(Rides[auxRide])

f = open("b_should_be_easy.in","r")
line = f.readline()
R,C,nbCars,nbRides,Bonus,Steps = list(map(int,line.strip().split()))

Cars = []
ACars=[]
for i in range(nbCars):
    Cars.append(car(i))
    ACars.append(i)

Rides = []
for i in range(nbRides):
    line = f.readline()
    sx, sy, fx, fy, es, lf = list(map(int,line.strip().split()))
    R = Ride(i,sx, sy, fx, fy, es, lf)
    Rides.append(R);
while(Rides):
    assignRideCar(Cars,Rides,Bonus,ACars)
#showRide(Rides)
showCars(Cars)
