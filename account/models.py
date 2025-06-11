from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    avatar = models.ImageField(null=True, blank=True, verbose_name='Avatar')


    def __str__(self):
        return self.user.username