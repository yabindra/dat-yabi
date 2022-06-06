from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'base/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')




def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('user_login')

    else:
        f = CustomUserCreationForm()

    return render(request, 'base/register.html', {'form': f})


def home(request):
    return render (request, 'base/home.html')