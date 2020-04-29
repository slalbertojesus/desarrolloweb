from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from .forms import CreateUserForm 

def display_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
                form.save()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def display_singin(request):
    context = {}
    return render(request, 'accounts/home.html', context)

