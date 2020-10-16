from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.
def procesos(request):
    data = {
        'procesos':listar_procesos_ejecutados(),
        'tareatipo':listar_tareas_tipo(),
        'cantareas':cantidad_de_tareas(),
        'terminadas':tareas_terminadas(),
        'en_curso':tareas_en_curso(),
        'detenidas':tareas_detenidas()
        }
  

    return render(request, 'DashboardCliente/dashboard.html',data)


def listar_procesos_ejecutados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_PROCESO_EJECUTADO', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 
    
def listar_tareas_tipo():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_TAREA_TIPO', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 

def cantidad_de_tareas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_CANTIDAD_TAREAS', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 

def tareas_terminadas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_CANTAREAS_TERMINO', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 

def tareas_en_curso():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_CANTAREAS_ENCURSO', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista
def tareas_detenidas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_CANTAREAS_DETENIDAS', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def get_grafico_cantidad(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['dashboard']='dashboard'
    context['cantidad_de_tareas']=self.cantidad_de_tareas()
    return context    