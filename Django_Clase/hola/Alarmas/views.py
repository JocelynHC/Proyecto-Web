from django.shortcuts import render


Alarmas= ['5:30', '5:35', '5:40', '5:50']
# Create your views here.
def index(request):
    return render(request, 'Alarmas/index.html', {'Alarmas':Alarmas})
