from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='login')
def home (request):
    return render(request,'index.html')

@login_required(login_url='login')
def profile(request):

    object = get_object_or_404(Profile, pk='422180')
    return render(request,'profile.html',{'object': object})

@login_required(login_url='login')
def result(request):
    return render(request,'result.html')

@login_required(login_url='login')
def sem(request):
    return render(request,'sem.html')