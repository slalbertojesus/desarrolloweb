import re
import random 
import hashlib
import json

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import Http404
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import BSModalLoginView 
from bootstrap_modal_forms.generic import BSModalUpdateView
from bootstrap_modal_forms.generic import  BSModalCreateView
from bootstrap_modal_forms.generic import BSModalDeleteView
from accounts.models import EmailConfirmed, PasswordReset


from .models import Account 
from .forms import AccountForm, AccountUpdateForm, SetCustomPasswordForm, CreateUserForm, AuthenticationForm, AccountCreationForm

User = get_user_model()

def display_home(request):
    context = {}
    return render(request, 'accounts/home.html', context)

def display_register(request):
    if request.user.is_superuser: 
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
            password_already_forgotten, password_reset_created = PasswordReset.objects.get_or_create(user=user)
            if password_reset_created:
                short_hash = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
                reset_key = hashlib.sha1((short_hash+username).encode('utf-8')).hexdigest()
                password_already_forgotten.reset_key = reset_key
                password_already_forgotten.save()
                password_already_forgotten.send_password_reset_email()
                message = "Se ha mandado un mensaje al correo "
                messages.info(request, message)
            else:
                message = "No se ha podido enviar el correo "
                messages.info(request, message)
    context = {}
    return render(request, 'accounts/password_reset.html', context)

def restore_password_key_view(request, password_key_provided):
    if SHA1_RE.search(password_key_provided):
        message = ''
        try:
            password_change =  PasswordReset.objects.get(reset_key = password_key_provided)
            user = password_change.user
            account = None
            account = User.objects.get(username=user.username)
        except PasswordReset.DoesNotExist:
            password_change = None
            raise Http404
        if password_change is not None:
            form = SetCustomPasswordForm(request.user, request.POST)
            if request.method == 'POST':
                if form.is_valid():
                    password = form.cleaned_data.get('new_password1')
                    account.set_password(password)
                    if account is not None: 
                        account.save()
                        password_change.reset_key = ""
                        password_change.save()
                        messages.success(request, 'La contraseña ha sido cambiada satisfactoriamente.')
                        return redirect('/login')
                else:
                    message ='La contraseña no se ha podido cambiar'
        else:
            message = 'El link es inválido, por favor envía un nuevo formulario para cambiar su contraseña'
    else: 
        raise Http404
    context = {'form':form, "message": message}
    return render(request, 'accounts/password_forgotten.html', context)

def error_404_view(request, exception):
    return render(request, 'accounts/404.html')

@login_required
def accounts_view(request):
    accounts = User.objects.all()
    context = {'accounts':accounts}
    return render(request, 'accounts/accounts_crud.html', context)

class LogIn(BSModalLoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/modals/login_modal.html'
    success_message = 'Se inicio sesión satisfactoriamente.'
    extra_context = dict(success_url=reverse_lazy('accounts:home'))

class CreateAccount(BSModalCreateView):
    form_class = AccountCreationForm
    success_message = 'Se ha creado un usuario con éxito'
    template_name = 'accounts/modals/create_modal.html'
    success_url = reverse_lazy('accounts:accounts')
 
class UpdateAccount(BSModalUpdateView):
    model = User
    form_class = AccountUpdateForm
    success_message = 'Se ha actualizado con éxito'
    template_name = 'accounts/modals/update_modal.html'
    success_url = reverse_lazy('accounts:accounts')

class DeleteAccount(BSModalDeleteView):
    model = User
    success_message = 'Se ha eliminado con éxito'
    template_name = 'accounts/modals/delete_modal.html'
    success_url = reverse_lazy('accounts:accounts')

def logout_user(request):
    logout(request)
    return redirect('/login')