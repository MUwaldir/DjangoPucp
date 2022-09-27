from . import views
from django.urls import path

app_name = 'examenFinal'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('obtener_info_tarea',views.obtener_info_tarea, name='tarea_info'),
    path('nuevaTarea', views.nuevaTarea, name='nuevaTarea'),
    path('eliminarTarea',views.eliminarTarea, name='eliminarTarea'),
    path('editarTarea', views.editarTarea, name='editarTarea'),
    path('actualizarTarea/<str:tarea_id>', views.actualizarTarea, name="actualizarTarea"),
]