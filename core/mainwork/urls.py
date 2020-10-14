from django.urls import path
from .views import index, logged_in, usuarios, empresa, empresas, proceso, tarea, unidad, unidades, procesos


urlpatterns = [
    path('', index, name="index"),
    path('logged_in/', logged_in),
    path('usuarios/', usuarios, name="lista_usuarios"),
    path('empresa/', empresa, name="empresa"),
    path('unidad/', unidad, name="unidad"),
    path('proceso/', proceso, name="proceso"),
    path('tareas/', tarea, name="tarea"),
    path('listaempresa/', empresas, name="lista_empresa"),
    path('listaunidades/', unidades, name="lista_unidad"),
    path('listaprocesos/',procesos, name="lista_procesos")


    
]
