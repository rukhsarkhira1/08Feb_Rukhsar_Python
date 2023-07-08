from django.shortcuts import render,redirect
from .forms import userform
from .models import userdata

# Create your views here.
def index(request):
    if request.method=="POST":
        user=userform(request.POST)
        if user.is_valid():
            user.save()
            print("Records have been added successfully... ")
            return redirect('showdata')
        else:
            print(user.errors)

    return render(request,'index.html')
def showdata(request):
    data=userdata.objects.all()
    return render(request,'showdata.html',{'data':data})