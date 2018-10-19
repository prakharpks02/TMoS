from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home
from django.contrib.auth.decorators import login_required
import json as simplejson, urllib


@login_required
def rtms(request):
    sourcedistance = {}
        
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            Home = form.save()
            Source=Home.source
            Destination1=Home.destination1
            Destination2=Home.destination2
            Destination3=Home.destination3
            Destination4=Home.destination4
            Destination5=Home.destination5
            Destination6=Home.destination6
            Destination7=Home.destination7
            Destination8=Home.destination8
            Destination9=Home.destination9
            Destination10=Home.destination10
            number=Home.no_of_destinations
            Weight = number*[0]
            Weight[0]=Home.weight1
            Weight[1]=Home.weight2
            Weight[2]=Home.weight3
            Weight[3]=Home.weight4
            Weight[4]=Home.weight5
            Weight[5]=Home.weight6
            Weight[6]=Home.weight7
            Weight[7]=Home.weight8
            Weight[8]=Home.weight9
            Weight[9]=Home.weight10
            Home.save()
            GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
            API_KEY = 'AIzaSyC7g11CKYY1xfnx-_Ofv59oSuDAIqH8e1A'
            time = 'now'

            url = GEOCODE_BASE_URL + '?' + 'origins=' + Source +'&destinations=' + Destination1 + '|' + Destination2 + '|' + Destination3 + '|' + Destination4 + '|' + Destination5 + '|' + Destination6 + '|' + Destination7 + '|' + Destination8 + '|' + Destination9 + '|' + Destination10 + '&mode=driving&traffic_model=best_guess&departure_time=' + time + '&language=en-En&key=' + API_KEY
            result = simplejson.load(urllib.request.urlopen(url))
            
            
            for i in range(number):
                sourcedistance[i+1] =result['rows'][0]['elements'][i]['distance']['value']
            for i in range(number,10):
                sourcedistance[i+1] = "Form is not filled for this destination"
            sdmatrix = number*[0]
            for i in range(number):
                sdmatrix[i] = sourcedistance['i+1']
            weightF = number*[0]
            for i in range(number):
                weightF[i] = Weight[i]

    else:
        form = HomeForm()
        Source="Nothing filled yet"
        Destination1="Nothing filled yet"
        Destination2="Nothing filled yet"
        Destination3="Nothing filled yet"
        Destination4="Nothing filled yet"
        Destination5="Nothing filled yet"
        Destination6="Nothing filled yet"
        Destination7="Nothing filled yet"
        Destination8="Nothing filled yet"
        Destination9="Nothing filled yet"
        Destination10="Nothing filled yet"
        result = "Form not filled yet"
        for i in range(10):
            sourcedistance[i+1] ="Form is not filled for this destination"

    
    context={'form':form, 'Source':Source, 'Destination1':Destination1, 'Destination2':Destination2, 'Destination3':Destination3, 'Destination4':Destination4, 'Destination5':Destination5,
     'Destination6':Destination6, 'Destination7':Destination7, 'Destination8':Destination8, 'Destination9':Destination9, 
     'Destination10':Destination10, 'result':result, 'distance1':sourcedistance[1], 'distance2':sourcedistance[2],
     'distance3':sourcedistance[3], 'distance4':sourcedistance[4], 'distance5':sourcedistance[5], 'distance6':sourcedistance[6],
     'distance7':sourcedistance[7], 'distance8':sourcedistance[8], 'distance9':sourcedistance[9], 'distance10':sourcedistance[10]}
    return render(request, 'Manager/fleet.html', context)




    """def looperBeta(noOfSources, capacityOfTruck, weightF, distancesToW, DistMatrix) :
    
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
        print("The possibilities now are : ",possibilities)
        print("I am at ", k)
        
        # 3.01 If they have no possibilities to go to and sources are left on the map, go to warehouse
        if len(possibilities) == 0 :
            
            DistByTruck += distancesToW[k]
            distByTrucks.append(DistByTruck)
            
            loadByTrucks.append(LoadByTruck)
            
            roundsByTruck += 1
            
            print("Going to Warehouse from ", k)
            
            LoadByTruck = 0     
            continue

        # 4. Find the nearest source amongst them
        closestSource, closestDistance = myNeighbour(k, DistMatrix, possibilities)
        print("ClosestNeighbour : ", closestSource)

        # 5. Update the dist and load values
        DistByTruck += closestDistance
        LoadByTruck += weightF[closestSource]
        
        print("Total Distance Travelled till now : ",DistByTruck)
        print("Total load carried on now : ",LoadByTruck)

        # 6. Delete the previous point k and update k
        DistMatrix, weightF, distancesToW = deletePoints(k, DistMatrix, weightF, distancesToW)
        if k > closestSource :
            k = closestSource
        elif k < closestSource :
            k = closestSource - 1
        
        noOfSources = len(weightF)
    
    DistByTruck += distancesToW[k]
    
    return LoadByTruck, DistByTruck, roundsByTruck"""