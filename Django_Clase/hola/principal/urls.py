from django.urls import path
from . import views

urlpatterns=[
    path("", views.holaDjango, name="holaDjango"),
    path('pepe', views.pepe, name="holapepe"),
    path('indice', views.indice, name='indice'),
    path('indice/<str:name>', views.indiceParam, name='indiceParam'),
    path('<str:name>', views.holaTu, name='holaTu'),
    
]
