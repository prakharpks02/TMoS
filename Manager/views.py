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