from django.shortcuts import render, redirect
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home
from django.contrib.auth.decorators import login_required


@login_required
def rtms(request):
    
        
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
            Home.save()
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

    
    context={'form':form, 'Source':Source, 'Destination1':Destination1,
     'Destination2':Destination2, 'Destination3':Destination3, 'Destination4':Destination4, 'Destination5':Destination5,
     'Destination6':Destination6, 'Destination7':Destination7, 'Destination8':Destination8, 'Destination9':Destination9, 
     'Destination10':Destination10, }
    return render(request, 'Manager/fleet.html', context)

    
