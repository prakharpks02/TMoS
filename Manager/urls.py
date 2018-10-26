from django.contrib import admin
#from django.urls import include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.rtms, name='rtms'),
    
]