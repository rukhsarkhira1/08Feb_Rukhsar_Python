from django.contrib import admin
from .models import product_mst,product_sub_cat

class useradmin(admin.ModelAdmin):
    list_display=['id','product_name']
   

class another(admin.ModelAdmin):
     list_display=['price','image','product_model','ram']

# Register your models here.
admin.site.register(product_mst,useradmin)
admin.site.register(product_sub_cat,another)

