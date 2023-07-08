from django.shortcuts import render
from .models import product_mst,product_sub_cat
#from itertools import chain

# Create your views here.
def index(request):
    return render(request,'index.html')

def viewproduct(request):
    #combo=list(chain(product_mst,product_sub_cat))

    data2=product_sub_cat.objects.all()
    return render(request,'viewproduct.html',{'data2':data2})