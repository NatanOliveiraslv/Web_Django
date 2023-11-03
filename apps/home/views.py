from django.shortcuts import render

def index(request):
    return render(request, 'usuarios/index.html')

def cliente(request):
    return render(request, 'usuarios/cliente.html')

def categoria(request):
    return render(request, 'usuarios/categoria.html')