from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    pass

class PasswordReset(models.Model):
    user                      = models.OneToOneField(Account, on_delete=models.CASCADE)
    reset_key                 = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.user)

    def send_password_reset_email(self):
        reset_password_url = "http://localhost:8005/reset-link/" + self.activation_key 
        print("LLave de activación en el modelo: " + self.activation_key)
        context = {
            "activation_url": reset_key,
            "user": self.user.username,
        }
        message = render_to_string("accounts/reset_password_message.txt", context)
        subject = "Haz solicitado un cambio de contraseña." + self.user
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
 
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], kwargs)

class EmailConfirmed(models.Model):
    user                      = models.OneToOneField(Account, on_delete=models.CASCADE)
    activation_key            = models.CharField(max_length=200)
    confirmed                 = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.confirmed)

    def send_activation_email(self):
        activation_url = "http://localhost:8005/accounts/activate/" + self.activation_key 
        context = {
            "activation_url": activation_url,
            "user": self.user.username,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activa tu correo, por favor."
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
 
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], kwargs)


