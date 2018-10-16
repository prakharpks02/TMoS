from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^no_login$', views.no_login, name='no_login'),
    url(r'^$', csrf_exempt(views.login), name='login'),
]