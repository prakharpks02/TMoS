from django.shortcuts import render
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home


def rtms(request):
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            Home = form.save(commit=False)
            Source=Home.source
            Destination=Home.destination
            Home.author = request.user
            Home.save()
            #return redirect('')
    else:
        form = HomeForm()
        #Home=form()
        Source=None
        Destination=None

    #Source=Home.source()
    #Destination=Home.destination()
    context={'form':form, 'Source':Source, 'Destination':Destination, }
    return render(request, 'Manager/fleet.html', context)