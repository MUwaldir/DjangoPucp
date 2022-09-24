from . import views
from django.urls import path

app_name = 'pichangasApp'

urlpatterns = [
    path('',views.ingresar,name='ingresar'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('nuevaPichanga',views.nuevaPichanga,name='nuevaPichanga'),
    path('editarPichanga/<str:ind>',views.editarPichanga,name='editarPichanga'),
]