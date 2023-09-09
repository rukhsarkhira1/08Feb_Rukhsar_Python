from django.contrib import admin
from .models import Task

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['title','completed']

admin.site.register(Task,userAdmin)