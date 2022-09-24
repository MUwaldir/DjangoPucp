from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from userb.models import userb_info

# Create your views here.

def index(request):
    return render(request,'posts/index.html')

def posts(request):
    inicio = request.GET.get('inicio')
    final = request.GET.get('final')

    data = []
    for i in range(int(inicio), int(final)+1):
        usuario_capturado = userb_info.objects.get(id=i)
        info_usuarios = [usuario_capturado.nombre,usuario_capturado.apellido,usuario_capturado.direccion]
        data.append(info_usuarios)

    if int(final) > 15:
        data=[]

    return JsonResponse({
        'posts':data
    })