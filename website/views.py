import django
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import django.contrib.auth.models
from django.shortcuts import render, redirect
from .forms import AddRecordForm, LoginForm, SignUpForm
from .models import Record


# Create your views here.

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login

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
        form = LoginForm()
        return render(request, 'home.html', {'form':form, 'records': records})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def record_user(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record':record})
    else:
        messages.success(request, ('Please log in to view this record...'))
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST or None)
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user
                record.save()
                messages.success(request, ('Record has been added!'))
                return redirect('home')
        else:
            form = AddRecordForm()
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, ('Please log in to add a record...'))
        return redirect('home')
    
def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        if request.method == 'POST':
            form = AddRecordForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, ('Record has been edited!'))
                return redirect('home')
        else:
            form = AddRecordForm(instance=record)
            return render(request, 'edit_record.html', {'form':form})
    else:
        messages.success(request, ('Please log in to edit a record...'))
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, ('Record has been deleted!'))
        return redirect('home')
        # if request.method == 'POST':
        # else:
            # messages.success(request, ('Please select a record to delete...'))
            # return redirect('home')    
    else:
        messages.success(request, ('Please log in to delete a record...'))
        return redirect('home')