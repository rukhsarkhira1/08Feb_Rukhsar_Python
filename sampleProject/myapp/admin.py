from django.contrib import admin
from .models import userSignup

class userAdmin(admin.ModelAdmin):
    list_display=['firstname']

# Register your models here.
admin.site.register(userSignup,userAdmin)