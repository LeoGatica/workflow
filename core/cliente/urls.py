from django.urls import path
from .views import *


urlpatterns = [
    path('control/',procesos, name="lista_procesos"),
    path('controlger/',procesos_Gerente, name="lista_procesos_gerente"),
    path('controljef/',procesos_Jefe, name="lista_procesos_jefe"),
    path('controlpro/',procesos_Process, name="lista_procesos_process")



]

  
    
 