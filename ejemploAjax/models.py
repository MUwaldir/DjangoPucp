from django.db import models

# Create your models here.
class usuarioApp(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    edad = models.CharField(max_length=32,default='')
    direccion = models.CharField(max_length=256,default='')
    categoria = models.CharField(max_length=128,default='')