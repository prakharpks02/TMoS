from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def fleet(request):
    return render(request, 'fleet.html')
def map(request):
    return render(request, 'Google_Map.html')
def rtms(request):
    return render(request, 'RTMS.html')