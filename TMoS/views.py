from django.shortcuts import render
from django.http import HttpResponse
from Manager.forms import HomeForm
from Manager.models import Home

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def fleet(request):
    return render(request, 'Manager/fleet.html')
def map(request):
    return render(request, 'Manager/Google_Map.html')

