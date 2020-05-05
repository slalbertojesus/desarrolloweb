import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import render, redirect, Http404
from django.contrib.auth import get_user_model


from accounts.models import EmailConfirmed


from .forms import CreateUserForm 

User = get_user_model()

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

def activation_view(request, activation_key_provided):
    if SHA1_RE.search(activation_key_provided):
        try:
            user_confirmed =  EmailConfirmed.objects.get(activation_key = activation_key_provided)
        except EmailConfirmed.DoesNotExist:
            user_confirmed = None
            raise Http404
        if user_confirmed is not None and not user_confirmed.confirmed:
            message = "El correo ha sido confirmado correctamente."
            user_confirmed.confirmed = True
            user_confirmed.save()
        elif user_confirmed is not None and user_confirmed.confirmed:
            message = "El correo ya ha sido confirmado."
        else:
            message = ""

        context = {"message": message}
        return render(request, 'accounts/activation_complete.html', context)
    else: 
        raise Http404

def restore_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user =  User.objects.get(username = username)
        except User.DoesNotExist:
            user = None
            message = "El usuario no existe, verifica que es correcto"
            messages.info(request, message)
        if user is not None:
            #Se crea código usuario * correo * hora 
            #Se agrega ese código a modelo
            #Se manda correo
            message = "Se ha mandado un mensaje al correo "
            messages.info(request, message)
    context = {}
    return render(request, 'accounts/password_reset.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')


