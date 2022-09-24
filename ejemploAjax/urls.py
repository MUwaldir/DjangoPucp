from . import views
from django.urls import path

app_name = 'ejemplo_django'

urlpatterns = [
    path('',views.index,name='index'),
    path('cargarInformacion/<str:num>',views.cargarInformacion,name='cargarInformacion'),
    path('cargarInfoUsuario',views.cargarInfoUsuario,name='cargarInfoUsuario'),
    path('cargarUsuarios',views.cargarUsuarios,name='cargarUsuarios'),
    path('guardarUsuario',views.guardarUsuario,name='guardarUsuario'),
]