from email import message
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    email = models.CharField(max_length=100,null=False,blank=False)
    mobno = models.CharField(max_length=10,null=True,blank=True)
    message = models.TextField(max_length=500,null=True,blank=True)