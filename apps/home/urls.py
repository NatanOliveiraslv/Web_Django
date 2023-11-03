from django.urls import path
from . import views

urlpatterns = [
    path('categoria/', views.categoria, name='categoria'),
    path('cliente/', views.cliente, name='cliente'),
    path('', views.index, name='index'),
]