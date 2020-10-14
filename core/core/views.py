from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.
def procesos(request):
    
    data = {
        'procesos':listar_procesos(),
        'empresas':listar_empresas(),
        }
    if request.method == 'POST':
        id_proceso = request.POST.get('id_proceso')
        salida = ejecutarproceso(id_proceso)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            data['procesos'] =  listar_procesos()
        else:
            data['mensaje'] = 'No se pudo agregar'


    return render(request, 'Ejecucion/ejecutar_proceso_tarea_tipo.html',data)

def empresa_unidades_proceso(request):
    empresa_id =request.GET.get('empresa_id')
    data = {
           'unidades':listar_unidades(empresa_id)
        }    
    return render(request, 'unidades_empresas.html',data)

def unidades_proceso(request):
    unidad_id =request.GET.get('unidadId')
    data = {
           'procesos_tipo':listar_procesos_tipo(unidad_id)
        }    
    return render(request, 'unidades_procesos.html',data)

def procesos_tarea(request):
    proceso_id =request.GET.get('procesoid')
    data = {
           'procesos_tarea':listar_procesos_tareas_tipo(proceso_id)
        }    
    return render(request, 'Ejecucion/procesos_tareas.html',data)





def listar_procesos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_PROCESOS_EJECUTADOS', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def listar_empresas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_LISTAR_EMPRESAS', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 

def listar_unidades(idempresa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_UNIDADES',[out_cursor, idempresa])
   
    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def listar_procesos_tipo(idproceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_PROCESOS_UNIDADES',[out_cursor, idproceso])
   
    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def listar_procesos_tareas_tipo(idproceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_PROCESOS_TAREAS',[out_cursor, idproceso])
   
    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista


def ejecutarproceso(id_proceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ACTIVAR_PROCESO',[id_proceso, salida])
    return salida.getvalue()