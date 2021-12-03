from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def holaDjango(request):
    return HttpResponse("<h1>Hola Django!</h1>")

def pepe(request):
    return HttpResponse("<h1>Hola Pepe!</h1>")

def holaTu(request,name):
    return HttpResponse(f" Hola, {name.capitalize()}!😎")

def indice(request):
    return render(request, "principal/index.html")

def indiceParam(request, name):
    return render(request, "principal/saludo.html", {"name":name.capitalize() #aqui podriamos pasar mas parametros
    })
