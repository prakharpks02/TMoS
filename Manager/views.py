from django.shortcuts import render
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home



def rtms(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = HomeForm(request.POST)
            if form.is_valid():
                Home = form.save(commit=False)
                Source=Home.source.all()
                Destination=Home.destination.all()
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

    else:
        return render(request, 'login/Not_Logged.html')