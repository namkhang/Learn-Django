from django.db import models

# Create your models here.
class Account(models.Model):
     id =models.IntegerField
     username = models.CharField(max_length = 200)
     password = models.CharField(max_length = 200)
     fullname = models.CharField(max_length = 200)

     @classmethod
     def create(cls , id , username , password , fullname):
         test_record = cls(id = id , username = username , password = password , fullname = fullname)   
         return test_record

     def save(self ,*args ,**kwargs):
         super().save(*args ,**kwargs)