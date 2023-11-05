from django.shortcuts import render
from clients.models import Client

def index(request):
    clientes = Client.objects.all()
    return render(request, 'usuarios/index.html', {"clienteDoDjango": clientes})

def cliente(request):
    return render(request, 'usuarios/cliente.html')

def categoria(request):
    return render(request, 'usuarios/categoria.html')