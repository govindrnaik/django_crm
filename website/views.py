from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from flask import redirect


# Create your views here.

def home(request):
    return render(request, 'home.html',{})


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if user has entered correct credentials
        user = authenticate(request, username=username, password=password)

        # If user has entered correct credentials
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - Please try again...'))
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

def register_user(request):
    pass