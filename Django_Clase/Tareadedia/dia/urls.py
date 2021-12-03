from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("viernes2", views.index2, name="index2")
]