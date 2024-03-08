from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login')
def home (request):
    return render(request,'index.html')

@login_required(login_url='accounts/login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='accounts/login')
def result(request):
    return render(request,'result.html')

@login_required(login_url='accounts/login')
def sem(request):
    return render(request,'sem.html')