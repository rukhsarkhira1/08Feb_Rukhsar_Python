from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('userlogout/',views.userlogut),
    path('home/',views.home,name='home'),
    path('register/',views.register),
    path('deletedata/<int:id>/',views.deletedata),

]