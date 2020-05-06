from django.contrib import admin
from accounts.models import EmailConfirmed, Account, PasswordReset

admin.site.register(EmailConfirmed)
admin.site.register(Account)
admin.site.register(PasswordReset)