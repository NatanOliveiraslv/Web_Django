from django.shortcuts import render
from clients.models import Client
from .forms import ClienteForm, CategoriaForm

def index(request):
    clientes = Client.objects.all()
    return render(request, 'usuarios/index.html', {"clienteDoDjango": clientes})

def cliente(request):
    sucesso = False
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Isso salva o cliente no banco de dados
             # Redirecionar para uma página de sucesso
            sucesso = True
    else:
        form = ClienteForm()
        
    return render(request, 'usuarios/cliente.html', {'sucesso': sucesso})

def categoria(request):
    sucesso = False
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # Isso salva o cliente no banco de dados
             # Redirecionar para uma página de sucesso
            sucesso = True
    else:
        form = CategoriaForm()
    return render(request, 'usuarios/categoria.html', {'sucesso': sucesso})