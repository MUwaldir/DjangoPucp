from django.shortcuts import render
from pichangasApp.models import pichanga_app, usuarios_app, equipo_app
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from dateutil.parser import parse

# Create your views here.

def ingresar(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuarios_app.objects.all()

        for usuario in usuarios_totales:
            if usuario.nombre == nombreUsuario and usuario.psw_usuario == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('pichangasApp:dashboard'))
        else:
            return render(request,'pichangasApp/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'pichangasApp/ingresar.html')

def dashboard(request):
    pichangas_totales = pichanga_app.objects.all()
    #Filtrar pichangas de nuestro equipo
    pichangas_equipo = []
    pichangas_locales = pichanga_app.objects.filter(equipo_local='1')
    for pichanga in pichangas_locales:
        pichangas_equipo.append(pichanga)
    pichangas_visitante = pichanga_app.objects.filter(equipo_visita='1')
    for pichanga in pichangas_visitante:
        pichangas_equipo.append(pichanga)
    #Filtrar finalizado
    return render(request,'pichangasApp/dashboard.html',{
        'objPichanga':pichangas_equipo,
    })

def nuevaPichanga(request):
    if request.method == 'POST':
        fechaPichanga = request.POST.get('fechaPichanga')
        fechaPichanga = parse(fechaPichanga)
        equipoLocal = request.POST.get('equipoLocal')
        equipoVisita = request.POST.get('equipoVisita')
        pichanga_app(fecha=fechaPichanga,equipo_local=equipoLocal,equipo_visita=equipoVisita).save()
        return HttpResponseRedirect(reverse('pichangasApp:dashboard'))
    return render(request,'pichangasApp/nuevaPichanga.html',{
        'equipos_registrados':equipo_app.objects.all()
    })

def editarPichanga(request,ind):
    pichanga_editar = pichanga_app.objects.get(id=ind)
    if request.method == 'POST':
        equipoLocal = request.POST.get('equipoLocal')
        equipoVisita = request.POST.get('equipoVisita')
        pichanga_editar.equipo_local = equipoLocal
        pichanga_editar.equipo_visita = equipoVisita
        pichanga_editar.save()
        return HttpResponseRedirect(reverse('pichangasApp:editarPichanga',kwargs={'ind':'2'}))
    return render(request,'pichangasApp/editarPichanga.html',{
        'pichanga_info' : pichanga_editar,
        'equipos_registrados':equipo_app.objects.all()
    })