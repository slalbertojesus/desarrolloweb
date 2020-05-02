from django.contrib import admin
from accounts.models import EmailConfirmed, Account

admin.site.register(EmailConfirmed)
admin.site.register(Account)