from django.urls import path, include

from .views import (
	display_home,
	display_login,
	display_register,
	logout_user,
	activation_view,
)

app_name = 'accounts'

urlpatterns = [
	path('', display_home, name="home"),
	path('login/', display_login, name="login"),
	path('register/', display_register, name="register"),
	path('logout/', logout_user, name="logout"),
	path('accounts/activate/<activation_key_provided>', activation_view, name="activation"),
]