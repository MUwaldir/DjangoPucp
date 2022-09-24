from . import views
from django.urls import path

app_name = 'userb'

urlpatterns = [
    path('',views.index,name='index'),
    path('posts',views.posts,name='posts'),
]