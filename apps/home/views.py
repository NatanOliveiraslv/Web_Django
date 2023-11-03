from django.shortcuts import render

def cliente(request):
    return render(request, 'usuarios/cliente.html')

def categoria(request):
    return render(request, 'usuarios/categoria.html')