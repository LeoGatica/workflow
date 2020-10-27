from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('procesos/', procesos, name="procesos"),
    path('unidades/', empresa_unidades_proceso , name="unidades_empresa"),
    path('procesos_tipo/', unidades_proceso , name="unidades_proceso"),
    path('procesos_tarea/',procesos_tarea , name="procesos_tareas"),
    path('ejecutarproceso/', procesos, name="ejecutar_proceso"),
    path('tareas/',tareas , name="tareas"),
    path('procesos_ejecutados/',procesos_ejecutados , name="procesos_ejecutados"),
    path('procesos_tarea/',procesos_tarea , name="procesos_tareas"),
    path('procesos_tarea_ejecutada/',procesos_tarea_ejecutadas , name="procesos_tarea_ejecutada"),

]