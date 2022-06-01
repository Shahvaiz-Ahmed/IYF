from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('register', views.register, name= 'register'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('objective', views.objective, name='objective'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('logoutuser', views.logoutuser, name='logoutuser')
]
