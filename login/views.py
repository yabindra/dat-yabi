from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def ulogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate( username = username, password = password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return  render(request, 'main/home.html')
            # return redirect('home')
            else:
                messages.error(request,'password and username are not match.')
                return redirect('ulogin')
        else:
            messages.error(request, 'password and username are not match')
            
    else:
        return render(request, 'main/login.html')
    
    
    

    
def register (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists.")
                return render(request, 'main/reg.html')
            else:
                user = User.objects.create_user(username=username,
                                          email=email,
                                        password=password1,)

                user.save()
                print(user)
                return redirect('ulogin')
        
        else:
            messages.info(request,"password not match")    
            return render(request, 'main/reg.html')
    
        
        
        
        
    else:
        return render(request, 'main/reg.html')
    
    
    
    
    
    
def main(request):
    return render(request, 'main/main.html')

    
@login_required
def home(request):
    return render(request, 'main/home.html')
    