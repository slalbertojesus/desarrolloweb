from django.urls import path, include

from .views import (
	display_singin,
	display_register,
)

app_name = 'accounts'

urlpatterns = [
	path('', display_singin, name="homepage"),
	path('register/', display_register, name="register"),
]