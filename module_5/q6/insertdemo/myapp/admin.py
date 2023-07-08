from django.contrib import admin
from .models import userdata

# Register your models here.
class useradmindata(admin.ModelAdmin):
    list_display=['id','name','email','mobile','address']
admin.site.register(userdata,useradmindata)
