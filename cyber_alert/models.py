from tkinter import CASCADE

from django.db import models

# Create your models here.
class AdminRegister(models.Model):
    adminid=models.CharField(max_length=50)
    name= models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

class GiverTransaction(models.Model):
    userid= models.ForeignKey(AdminRegister,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    aadharno = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    mobileno = models.CharField(max_length=50)
    bankname = models.CharField(max_length=50)
    accountno = models.CharField(max_length=50)
    branchname = models.CharField(max_length=50)
    amount = models.IntegerField()
    ifsccode = models.CharField(max_length=50)
    micrcode = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    transationid = models.CharField(max_length=50)
    countone=models.IntegerField(default=0)
