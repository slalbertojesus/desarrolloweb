import random 
import hashlib

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model


#Modelos
from accounts.models import EmailConfirmed

User = get_user_model()

@receiver(post_save, sender = User)
def account_post_save_signal(sender, instance, created,**kwargs):
    User = instance
    if created:
        email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=User)
        if email_is_created:
            short_hash = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            username = User.username
            activation_key = hashlib.sha1((short_hash+username).encode('utf-8')).hexdigest()
            print("Llave de activación en señal: "+activation_key)
            email_confirmed.activation_key = activation_key
            email_confirmed.save()
            email_confirmed.send_activation_email()

