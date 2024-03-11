from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.

def logout_page(request):
    logout(request)
    return redirect('login')

def login_page(request):

    # if request.method=='GET':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(username=username,password=password)

    #     if user is not None:
    #         login(request,user)
    #         return redirect('/')
    #     else: 
    #         messages.info(request,'Invalid credentials')
    #         return redirect('login')

    # else: 
    #     return render(request,'login.html')

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})


def register(request):
    # if request.method=='POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     username = request.POST.get('username')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     email = request.POST.get('email')

    #     if password1==password2:
    #         if User.objects.filter(email=email).exists():
    #             messages.info(request,'Email taken')
    #             return redirect('register')           
    #         else:
    #             user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
    #             user.set_password(password1)
    #             user.save()
    #             print('user created')
    #             return redirect('login')
    #     else:
    #         messages.info(request,'password not matching')
    #         return redirect('register')
    #     return redirect('/')
    # else:
    #     return render(request,'register.html')
    
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})