from django.db import models


# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()
    saddress=models.TextField()
    
