from django.urls import path, include

from .views import (
	display_home,
	display_login,
	display_register,
	logout_user,
)

app_name = 'accounts'

urlpatterns = [
	path('login/', display_login, name="login"),
	path('logout/', logout_user, name="logout"),
	path('register/', display_register, name="register"),
	path('', display_home, name="home"),
]