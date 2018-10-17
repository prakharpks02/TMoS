from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from login.models import Login
from login.forms import LoginForm

def no_login(request):
    return render(request, 'login/Not_Logged.html')


def login_view(request):
    #if request.method == 'POST':
    #    form = AuthenticationForm(request.POST)
    #    if form.is_valid():
    #        user = form.get_user()
    #       login(request,user)
    #        return redirect('rtms')
    #else:
    #    form=AuthenticationForm()
    #return render(request, 'login/login.html', {'form':form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)      
            if user is not None:
                login(request, user)
                return redirect('/rtms')
            else:
                return redirect('login/nologin')
    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form' : form})
