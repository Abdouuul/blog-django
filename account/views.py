from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.account.address = form.cleaned_data['address']
            return redirect('login')        
    return render(request, 'register.html', {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        if form.is_valid():
            login(request)
            return redirect('/')
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('/')
    