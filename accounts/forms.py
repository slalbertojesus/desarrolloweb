from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Usuario', 'required':'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Correo','required':'True'}),
    }

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite la contraseña'})

		