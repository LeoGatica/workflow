from django.urls import path
from .views import index, logged_in, clientes, empresa, empresas

urlpatterns = [
    path('', index, name="index"),
    path('logged_in/', logged_in),
    path('clientes/', clientes, name="clientes"),
    path('empresa/', empresa, name="empresa"),
    path('listaempresa/', empresas, name="lista_empresa")


    
]
