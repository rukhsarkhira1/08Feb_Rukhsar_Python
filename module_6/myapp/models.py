from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=300)
    Author=models.CharField(max_length=50)
    Isbn=models.BigIntegerField()
    Publisher=models.CharField(max_length=50)