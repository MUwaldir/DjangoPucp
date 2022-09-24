from django.db import models

# Create your models here.
class estudiante(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo = models.CharField(max_length=128,default='')
    direccion = models.CharField(max_length=128,default='')
    email = models.CharField(max_length=128,default='')