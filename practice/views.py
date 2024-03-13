from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student1,Course,Enrollment

# Create your views here.
@login_required(login_url='login')
def home (request):
    objects = Course.objects.all()
    return render(request,'index.html',{'objects':objects})

@login_required(login_url='login')
def profile(request):

    object = Student1.objects.get(user_name='user1')
    return render(request,'profile.html',{'object': object})

@login_required(login_url='login')
def result(request):
    obj = Student1.objects.get(pk='user3')
    current_sem = int(obj.semester)
    return render(request,'result.html',{'num_times':range(current_sem-1)})

@login_required(login_url='login')
def sem(request):
    queryset1 = Course.objects.all()
    queryset2 = Enrollment.objects.all()
    context = {'context': zip(queryset1,queryset2)}
    return render(request,'sem.html',context)