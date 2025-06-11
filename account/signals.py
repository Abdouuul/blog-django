from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Account

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    print('Bienvenu à {instance.firstname}!')
    if created:
        account = Account(user=instance)
        account.save()    
