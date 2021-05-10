from django.shortcuts import render
from django.http import HttpResponse, Http404
#from registro import models
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return HttpResponse('este es el index')

def home(request):
    return render(request, 'registro/home.html', context=None)

def actualizar_datos(request, nom):
    #definimos contexto para actualizar datos del que ya estaba loggeado
    user = User.objects.get(username=nom)
    conte = {'email': user.email, 'nombre': user.username, 'cui': user.profile.cui}
    return render(request, 'registro/editar_datos.html', context=conte)

def profile(request, nom):
    try:
        user = User.objects.get(username=nom)
        ctx = {'nombre': user.username, 'email': user.email, 'cui': user.profile.cui, 'profesion': user.profile.profesion}
        return render(request, 'registro/profile.html', context=ctx)
    except User.DoesNotExist:
        raise Http404('not found')

def create(request):
    return HttpResponse('este es el create')

def logged_out(request):
    return render(request, 'registration/salir.html', context = None)

def editar(request):
    return HttpResponse('aca deberia ir el formulario para cambiar datos')
