from django.urls import path
from . import views

urlpatterns=[
    path('<str:semana>', views.holaViernes, name='holaViernes'),

]