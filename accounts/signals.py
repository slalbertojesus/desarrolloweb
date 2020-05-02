from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


logger = logging.getLogger(__name__)

@receiver(post_save, sender = User)
def test_post_save_signal(sender, instance, created,**kwargs):
    if created:
        print(sender)
        print(instance)      
        print(User)
        print(created)

