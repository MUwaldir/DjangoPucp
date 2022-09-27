import json
from django.shortcuts import render
from django.urls import reverse


from .models import tareasExamen, usuariosFinal
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuariosFinal.objects.all()

        for usuario in usuarios_totales:
            if usuario.usuario == nombreUsuario and usuario.contra == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('examenFinal:dashboard'))
        else:
            return render(request,'examenFinal/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'examenFinal/ingresar.html')

def dashboard(request):
    return render(request,'examenFinal/dashboard.html',{
        'tareas_totales':tareasExamen.objects.all().order_by('id')
    })

def obtener_info_tarea(request):
   
    id_tarea = str(request.GET.get('tarea_id'))
    id_t =id_tarea.split('detalle')
    tarea = tareasExamen.objects.filter(id=id_t[1])
    tarea_info = []
    for info in tarea:
        tarea_info.append([info.fechaCreacion,info.fechaEntrega,info.descripcion,info.estadoTarea])

    return JsonResponse({
        'tareas':tarea_info
    })

def nuevaTarea(request):
    informacion = json.load(request)
    f_creacion= informacion.get('f_creacion')
    f_entrega = informacion.get('f_entrega')
    descripcion = informacion.get('descripcion')
    estado= informacion.get('estado')
    tareasExamen(fechaCreacion = f_creacion, fechaEntrega=f_entrega, descripcion=descripcion,estadoTarea=estado).save()   
    return JsonResponse({
        'info':'tarea aceptada'
    })
  
def eliminarTarea(request):
    id_tarea = str(request.GET.get('ta_id'))
    id_t =id_tarea.split('eliminar')
    tarea = tareasExamen.objects.filter(id=id_t[1])
    tarea.delete()
    return JsonResponse({
        'info':'tarea borrada'
    })

def editarTarea(request):
    id_tarea = str(request.GET.get('tarea_id'))
    id_t =id_tarea.split('editar')
    tarea = tareasExamen.objects.filter(id=id_t[1])
    tarea_info = []
    for info in tarea:
        tarea_info.append([info.fechaCreacion,info.fechaEntrega,info.descripcion,info.estadoTarea])

    return JsonResponse({
        'tareas':tarea_info
    })

def actualizarTarea(request, tarea_id):
    tarea_ac = tareasExamen.objects.get(id=tarea_id)
    print(tarea_ac)
    if request.method == 'POST':
        t_creacion = request.POST.get('fecha_creacion')
        t_entrega= request.POST.get('fecha_entrega')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        tarea_ac.fechaCreacion = t_creacion
        tarea_ac.fechaEntrega = t_entrega
        tarea_ac.descripcion = descripcion
        tarea_ac.estadoTarea = estado
        tarea_ac.save()
        return HttpResponseRedirect(reverse('examenFinal:dashboard'))

    return HttpResponseRedirect(reverse('examenFinal:dashboard'))
