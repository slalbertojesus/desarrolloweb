from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	error_messages = {
        'password_mismatch': "Las contraseñas no son iguales",
    }
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Usuario', 'required':'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Correo','required':'True'}),
    	}

		error_messages = {
            'username': {
				"unique": "El usuario ya existe",
                'required': "El usuario es obligatorio",
                'invalid': "El usuario es inválido",
				},
			'email': {
				"unique": "El correo ya existe",
                'required': "El correo es obligatorio",
                'invalid': "El correo es inválido",
				},
		}

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control',
		 'placeholder': 'Contraseña', 'required':'True'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',
		 'placeholder': 'Repite la contraseña', 'required':'True'})
		self.fields['password1'].error_messages = {
            'invalid': "No sea pendejo.",
            'required': "No sea meco.",
            'max_length': "La contraseña es inválida.",
			'min_length': 'Las contraseñas son diferentes.',
		}
		self.fields['password2'].error_messages = {
            'invalid': "No sea pendejo.",
            'required': "No sea meco.",
            'max_length': "La contraseña es inválida.",
			'min_length': 'Las contraseñas son diferentes.',
		}

		