import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect, Http404

from accounts.models import EmailConfirmed, Account


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
                messages.success(request, 'Cuenta creada para ' + user + ", confirma tu correo para poder iniciar sesión")
                return redirect('/login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def display_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
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

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print("La llave es real")
        context = {}
        return render(request, 'accounts/activation_complete.html', context)
    else: 
        raise Http404


def logout_user(request):
    logout(request)
    return redirect('/login')


