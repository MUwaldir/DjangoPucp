from pyexpat import model
from django.db import models

# Create your models here.

class userb_info(models.Model):
    nombre = models.CharField(max_length=256,default='')
    apellido = models.CharField(max_length=256,default='')
    direccion = models.CharField(max_length=256,default='')