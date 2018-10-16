from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from login.models import Login
from login.forms import LoginForm

def no_login(request):
    return render(request, 'login/Not_Logged.html')


def login(request):
    msg = []
    if request.method == "POST":
        form = LoginForm(request.POST)
        Login = form.save(commit=False)
        username=Login.username
        password=Login.password
        user = authenticate(username = username, password = password)      
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                msg.append("login successful")
            else:
                msg.append("disabled account")
        else:
            msg.append("invalid login")
    else:
        form = LoginForm()
        Login = form.save(commit=False)
        username=Login.username
        password=Login.password
        user = authenticate(username = username, password = password)      
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                msg.append("login successful")
            else:
                msg.append("disabled account")
        else:
            msg.append("invalid login")
    return render_to_response('login/login.html', {'errors' : msg, 'form' : form})
