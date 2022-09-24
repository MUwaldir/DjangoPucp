from django.db import models
import datetime

# Create your models here.
class usuarios_app(models.Model):
    nombre = models.CharField(max_length=128,default='')
    psw_usuario = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')
    celular = models.CharField(max_length=128,default='')
    equipo = models.CharField(max_length=128,default='')

class pichanga_app(models.Model):
    fecha = models.DateField(default=datetime.date.today)
    marcador_local = models.CharField(max_length=128,default='0')
    marcador_visita = models.CharField(max_length=128,default='0')
    equipo_local = models.CharField(max_length=128,default='0')
    equipo_visita = models.CharField(max_length=128,default='0')
    estadoPichanga = models.CharField(max_length=128,default='Programada')

class equipo_app(models.Model):
    nombre = models.CharField(max_length=128,default='')
    arquero = models.CharField(max_length=32,default='')
    defensa_1 = models.CharField(max_length=32,default='')
    defensa_2 = models.CharField(max_length=32,default='')
    volante_1 = models.CharField(max_length=32,default='')
    volante_2 = models.CharField(max_length=32,default='')
    volante_3 = models.CharField(max_length=32,default='')
    delantero_1 = models.CharField(max_length=32,default='')
    delantero_2 = models.CharField(max_length=32,default='')