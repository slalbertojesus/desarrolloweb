from django.urls import path, include
from django.contrib.auth import views

from .views import (
	#Navegación
	display_home,
	display_login,
	display_register,
	logout_user,

	#Procesos de cuenta
	activation_view,
	restore_password_view,
	restore_password_key_view,

	#Administración de cuentas del sistema
	accounts_view,

	#account_update_view,
	UpdateAccount,
	DeleteAccount,
)

app_name = 'accounts'

urlpatterns = [
	path('', display_home, name="home"),
	path('login/', display_login, name="login"),
	path('register/', display_register, name="register"),
	path('logout/', logout_user, name="logout"),

	path('accounts/activate/<activation_key_provided>', activation_view, name="activation"),
	path('reset-link/<password_key_provided>', restore_password_key_view, name="passwordkey"),
	path('restore-password/', restore_password_view, name="restore"),

	path('accounts/', accounts_view, name="accounts"),
	path('accounts/update/<pk>', UpdateAccount.as_view(), name="update"),
	path('accounts/delete/<pk>', DeleteAccount.as_view(), name='delete'),
]