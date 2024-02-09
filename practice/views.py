from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'index.html')
def profile(request):
    return render(request,'profile.html')
# def login(request):
#     return render(request,'login.html')
def result(request):
    return render(request,'result.html')
def sem(request):
    return render(request,'sem.html')