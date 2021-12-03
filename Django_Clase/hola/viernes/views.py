from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def holaViernes(request,semana):
    return HttpResponse(f" Hoy es viernes, {semana.capitalize()}!😎")