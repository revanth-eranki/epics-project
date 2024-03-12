from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student1

# Create your views here.
@login_required(login_url='login')
def home (request):
    # object = get_object_or_404(Student1, pk='user1')
    return render(request,'index.html')

@login_required(login_url='login')
def profile(request):

    object = get_object_or_404(Student1, pk='user1')
    return render(request,'profile.html',{'object': object})

@login_required(login_url='login')
def result(request):
    return render(request,'result.html')

@login_required(login_url='login')
def sem(request):
    return render(request,'sem.html')