from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def gestion_propietario(request):
    return HttpResponse("coquito")


def gestion_propietario_Copy(request):
    return render(request, 'Registrar_usuario.html')