import numpy as np
from Manager.FuelConsumption import FuelConsumption
from Manager.FuelConsumption import FuelConsumptionStoD


def findSource(weightF) :
    k = weightF.index(max(weightF))
    return k


def findPoss(k, leftWeight, weightF) :                               # Find possibles for a particular k, leftWeight, weightF  
    possibles = []
    for i in range(len(weightF)) :
        if weightF[i] <= leftWeight and i != k and weightF[i] != 0 :
            possibles.append(i)
    return possibles

def myNeighbour(k, DistMatrix, possibles) :                                             # This function gives output of nearest source point and the distance of that source from the initial point of the function
    closestDist = 10000                                                                 # Just arbit out of the range number    
    closestNeighbour = 0
    
    for j in range(len(possibles)) :
        t = DistMatrix[k][possibles[j]]
        
        
        if t < closestDist :
            closestDist = t
            closestNeighbour = possibles[j]            
    
    return closestNeighbour, closestDist

def deletePoints(k, DistMatrix, weightF, distancesToW) :
    DistMatrix = np.delete(DistMatrix, (k) , axis = 0)
    DistMatrix = np.delete(DistMatrix, (k) , axis = 1)
    weightF = np.delete(weightF, k)
    distancesToW = np.delete(distancesToW, k)
    
    return DistMatrix, weightF, distancesToW

# Main Function starts here!!!!!

def looperBeta(noOfSources, capacityOfTruck, weightF, distancesToW, DistMatrix) :

    # 1. Initializing the variables
    LoadByTruck, DistByTruck, roundsByTruck = 0, 0, 0

    # 2. Lets select a starting point (if at warehouse use this in the loop)
    k = findSource(weightF)
    print("Start point : ", k)

    distByTrucks = []
    loadByTrucks = []

    LoadByTruck += weightF[k]
    DistByTruck += distancesToW[k]

    # So the loop starts from here :

    while noOfSources > 1 : 

        if DistByTruck == 0 :
            k = findSource(weightF)
            LoadByTruck += weightF[k]
            DistByTruck += distancesToW[k]
        
        # 3. See the possibilities to go to
        leftWeight = capacityOfTruck - LoadByTruck
        possibilities = findPoss(k, leftWeight, weightF)
        #print("The possibilities now are : ",possibilities)
        #print("I am at ", k)
        
        # 3.01 If they have no possibilities to go to and sources are left on the map, go to warehouse
        if len(possibilities) == 0 :
            
            DistByTruck += distancesToW[k]
            distByTrucks.append(DistByTruck)
            
            loadByTrucks.append(LoadByTruck)
            
            roundsByTruck += 1
            
            #print("Going to Warehouse from ", k)
            
            LoadByTruck = 0     
            continue

        # 4. Find the nearest source amongst them
        closestSource, closestDistance = myNeighbour(k, DistMatrix, possibilities)
        #print("ClosestNeighbour : ", closestSource)

        # 5. Update the dist and load values
        DistByTruck += closestDistance
        LoadByTruck += weightF[closestSource]
        
        #print("Total Distance Travelled till now : ",DistByTruck)
        #print("Total load carried on now : ",LoadByTruck)

        # 6. Delete the previous point k and update k
        DistMatrix, weightF, distancesToW = deletePoints(k, DistMatrix, weightF, distancesToW)
        if k > closestSource :
            k = closestSource
        elif k < closestSource :
            k = closestSource - 1

        noOfSources = len(weightF)

    DistByTruck += distancesToW[k]

    return LoadByTruck, DistByTruck, roundsByTruck