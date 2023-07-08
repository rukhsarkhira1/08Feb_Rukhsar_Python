from django.db import models


# Create your models here.
class product_mst(models.Model):
    product_name=models.CharField(max_length=20)
   
    
    def __str__(self) -> str:
        return self.product_name




class product_sub_cat(models.Model):
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='static/')
    product_model=models.CharField(max_length=20)
    ram=models.CharField(max_length=6)

    added_by=models.ForeignKey(product_mst,on_delete=models.DO_NOTHING)

