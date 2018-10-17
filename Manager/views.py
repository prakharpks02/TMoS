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
            Destination=Home.destination
            Home.save()
    else:
        form = HomeForm()
        Source="Nothing filled yet"
        Destination="Nothing filled yet"

    
    context={'form':form, }#'Source':Source, 'Destination':Destination, }
    return render(request, 'Manager/fleet.html', context)

    
