from django.db import models

# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    mobile=models.BigIntegerField()
    address=models.TextField()
'''
    def __str__(self) -> str:
        return self.name'''