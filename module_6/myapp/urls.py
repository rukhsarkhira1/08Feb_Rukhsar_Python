from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('getall/',views.getall),
    path('getid/<int:id>',views.getid),
    path('savedata/',views.savedata),
    path('deleteid/<int:id>',views.deleteid),
    path('updatedata/<int:id>',views.updatedata),
    
]