from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, label='Email')
    address = forms.CharField(required=False, label='Address')
    avatar = forms.ImageField(required=False, label='Avatar')
    
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}
