from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('',views.home),
    path('home/', views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('mark/',views.mark,name='mark'),
    path('display/',views.display),
]
