from tkinter import CASCADE

from django.db import models

# Create your models here.
from cyber_alert.models import GiverTransaction


class Sendquery(models.Model):
    transid=models.ForeignKey(GiverTransaction,on_delete=models.CASCADE)
    sendquery=models.CharField(max_length=400)
    name=models.CharField(max_length=100)