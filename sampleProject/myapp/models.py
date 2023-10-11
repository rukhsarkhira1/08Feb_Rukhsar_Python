from django.db import models
from datetime import datetime

# Create your models here.
class userSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    mobile=models.BigIntegerField()
    country=models.CharField(max_length=20)

class notes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    query=models.CharField(max_length=250)
    technology=models.CharField(max_length=30)
    file=models.FileField(upload_to='query')
    comments=models.TextField()

class contact(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    cntname=models.CharField(max_length=50)
    cntemail=models.EmailField()
    cntmobile=models.BigIntegerField()
    cntmessage=models.TextField()