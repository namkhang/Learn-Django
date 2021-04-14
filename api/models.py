from django.db import models

# Create your models here.
class Account(models.Model):
     id =models.IntegerField
     username = models.CharField(max_length = 200)
     password = models.CharField(max_length = 200)
     fullname = models.CharField(max_length = 200)
     image = models.CharField(max_length=200 , null= True)
