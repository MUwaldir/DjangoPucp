from django.db import models

# Create your models here.
class usuariosFinal(models.Model):
    usuario = models.CharField(max_length=256,default='')
    contra = models.CharField(max_length=256,default='')

class tareasExamen(models.Model):
    fechaCreacion = models.CharField(max_length=256,default='24-09-2022')
    fechaEntrega = models.CharField(max_length=256,default='30-09-2022')
    descripcion = models.CharField(max_length=512,default='')
    estadoTarea = models.CharField(max_length=128,default='PROGRESO')