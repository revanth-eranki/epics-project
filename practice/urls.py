from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name='profile'),
    path('result/',views.result,name='result'),
    path('sem/',views.sem,name='sem')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)