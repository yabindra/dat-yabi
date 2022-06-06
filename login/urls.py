from django.urls import path
from .import views

urlpatterns= [
    path('ulogin', views.ulogin, name='ulogin'),
    path('register',views.register, name='register'),
    path('home',views.home, name='home'),
    path('', views.main, name='main'),
]