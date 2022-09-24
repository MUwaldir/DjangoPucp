from . import views
from django.urls import path

app_name = 'ejemplo_django'

urlpatterns = [
    path('',views.index,name='index'),
    path('hola',views.hola,name='hola'),
    path('hastaLuego',views.hastaLuego,name='hastaLuego'),
    path('usuarioInfo',views.usuarioInfo,name='usuarioInfo'),
]