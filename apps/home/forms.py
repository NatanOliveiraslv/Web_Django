from django import forms
from clients.models import Client
from categories.models import Category

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'address', 'cell_phone', 'email', 'gender']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
