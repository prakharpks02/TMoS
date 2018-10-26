"""from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home
from django.contrib.auth.decorators import login_required
import json as simplejson, urllib
import numpy as np
from Manager.Code import looperBeta
from Manager.FuelConsumption import FuelConsumption
from Manager.FuelConsumption import FuelConsumptionStoD"""

"""
@login_required
def rtms(request):
    distancesToW = numberOfSources*[0]
        
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            Home = form.save()
            Source=Home.source
            #Destination = 10*[0]
            Destination1=Home.destination1
            destination2=Home.destination2
            Destination3=Home.destination3
            Destination4=Home.destination4
            Destination5=Home.destination5
            Destination6=Home.destination6
            Destination7=Home.destination7
            Destination8=Home.destination8
            Destination9=Home.destination9
            Destination10=Home.destination10
            numberOfSources=Home.no_of_destinations
            Weight = 10*[0]
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
            capacityOfTruck = Home.capacityOfTruck
            Home.save()
            Dist_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
            Elevation_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json'
            Geo_Base_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
            API_KEY = 'AIzaSyC7g11CKYY1xfnx-_Ofv59oSuDAIqH8e1A'
            time = 'now'

            url = Dist_BASE_URL + '?' + 'origins=' + Source +'&destinations=' + Destination1 + '|' + Destination2 + '|' + Destination3 + '|' + Destination4 + '|' + Destination5 + '|' + Destination6 + '|' + Destination7 + '|' + Destination8 + '|' + Destination9 + '|' + Destination10 + '&mode=driving&traffic_model=best_guess&departure_time=' + time + '&language=en-En&key=' + API_KEY
            result = simplejson.load(urllib.request.urlopen(url))

            url_des = Dist_BASE_URL + '?' + 'origins=' + Destination1 + '|' + Destination2 + '|' + Destination3 + '|' + Destination4 + '|' + Destination5 + '|' + Destination6 + '|' + Destination7 + '|' + Destination8 + '|' + Destination9 + '|' + Destination10 +'&destinations=' + Destination1 + '|' + Destination2 + '|' + Destination3 + '|' + Destination4 + '|' + Destination5 + '|' + Destination6 + '|' + Destination7 + '|' + Destination8 + '|' + Destination9 + '|' + Destination10 + '&mode=driving&traffic_model=best_guess&departure_time=' + time + '&language=en-En&key=' + API_KEY
            result_des = simplejson.load(urllib.request.urlopen(url_des))
            
            url_geo = Geo_Base_URL + '?address=' + Destination1 + '|' + Destination2 + '|' + Destination3 + '|' + Destination4 + '|' + Destination5 + '|' + Destination6 + '|' + Destination7 + '|' + Destination8 + '|' + Destination9 + '|' + Destination10 + '|' + Source + '&key=' + API_KEY
            result_geo = simplejson.load(urllib.request.urlopen(url_geo))

            for i in range(numberOfSources):
                destinationlat[i] = result_geo['geometry']['location']['lat']
                destinationlng[i] = result_geo['geometry']['location']['lng']

            thetadest = [[0 for x in range(numberOfSources)] for y in range(numberOfSources)]
            
            for i in range(numberOfSources):
                for j in range(numberOfSources):
                    url_ele = Elevation_BASE_URL + '?' + 'locations=' + destinationlat[i] +','+ destinationlng[i] + '|' + destinationlat[j] +','+ destinationlng[j] + '&key=' + API_KEY
                    result_ele = simplejson.load(urllib.request.urlopen(url_ele))
                    ele[i] = result_ele['results'][0]['elevation']
                    ele[j] = result_ele['results'][1]['elevation']
                    thetadest[i][j] = atan()
            
            for i in range(numberOfSources):
                distancesToW[i] =result['rows'][0]['elements'][i]['distance']['value']
            for i in range(numberOfSources,10):
                distancesToW[i+1] = "Form is not filled for this destination"

            weightF = numberOfSources*[0]
            for i in range(numberOfSources):
                weightF[i] = Weight[i]
           
            DistMatrix = [[0 for x in range(numberOfSources)] for y in range(numberOfSources)]
            for i in range(numberOfSources):
                for j in range(numberOfSources):
                    DistMatrix[i][j] =result_des['rows'][i]['elements'][j]['distance']['value']

            for i in range(numberOfSources):
                for j in range(numberOfSources):
                    t1[i][j] =result_des['rows'][i]['elements'][j]['duration_in_traffic']['value']
            for i in range(numberOfSources):
                for j in range(numberOfSources):
                    V1[i][j] =DistMatrix[i][j]/t1[i][j]
           
            print(result_des)
            print(DistMatrix)
            print(weightF)
            print(distancesToW)

            noOfSources=numberOfSources
            params = 0.001, 1, 9.81, 3, 0.57, 0.35, 46*(10**6), 0.832
            FC1 = FuelConsumption(V, t1, M, theta, params)

            LoadByTruck, DistByTruck, roundsByTruck = looperBeta(noOfSources, capacityOfTruck, weightF, distancesToW, DistMatrix)


    """        
"""
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
        result_des = "Form not filled yet"
        for i in range(10):
            sourcedistance[i+1] ="Form is not filled for this destination"
        LoadByTruck = "Fill the Form"
        DistByTruck = "Fill the Form"
        roundsByTruck = "Fill the Form"""


    #context={'form':form,} #"""'Load':LoadByTruck, 'Dist':DistByTruck, 'No_of_rounds':roundsByTruck"""
    #"""'Source':Source, 'Destination1':Destination1, 'Destination2':Destination2, 'Destination3':Destination3, 'Destination4':Destination4, 'Destination5':Destination5,
     #'Destination6':Destination6, 'Destination7':Destination7, 'Destination8':Destination8, 'Destination9':Destination9, 
    # 'Destination10':Destination10, 'result':result, 'distance1':sourcedistance[1], 'distance2':sourcedistance[2],
     #'distance3':sourcedistance[3], 'distance4':sourcedistance[4], 'distance5':sourcedistance[5], 'distance6':sourcedistance[6],
    # 'distance7':sourcedistance[7], 'distance8':sourcedistance[8], 'distance9':sourcedistance[9], 'distance10':sourcedistance[10],"""
     
    #return render(request, 'Manager/fleet.html', context)

 