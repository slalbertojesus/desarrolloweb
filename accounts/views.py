from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages

from .forms import CreateUserForm 

def display_home(request):
    context = {}
    return render(request, 'accounts/home.html', context)

def display_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada para' + user)
                return redirect('/login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def display_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None: 
            login(request, user)
            return redirect('/')
        else: 
            messages.info(request, 'Usuario o contraseña es incorrecta')
    context = {}
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')

