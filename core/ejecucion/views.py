from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.
def procesos(request):
    data = {
        'empresas':listar_empresas(),
        }
    if request.method == 'POST':
        id_proceso = request.POST.get('id_proceso')
        salida = ejecutarproceso(id_proceso)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
        else:
            data['mensaje'] = 'No se pudo agregar'
    return render(request, 'Ejecucion/ejecutar_proceso_tarea_tipo.html',data)

#termina la tarea
def tareas(request):
    data = {
        'empresas':listar_empresas()
        }
    if request.method == 'POST':
        idtarea = request.POST.get('tareas_e')
        idproceso = request.POST.get('procesos_e')
        salida = terminar_tarea(idtarea)
        salida2 = recalcular_proceso(idproceso)
        salida3 = recalcular_tarea(idproceso)

        if salida == 1:
            data['mensaje'] = 'Terminar Tarea'
        else:
            data['mensaje'] = 'No se pudo terminar'
    return render(request, 'Ejecucion/terminar_tarea.html',data)



def empresa_unidades_proceso(request):
    empresa_id =request.GET.get('empresa_id')
    data = {
           'unidades':listar_unidades(empresa_id)
        }    
    return render(request, 'Ejecucion/unidades_empresas.html',data)

def unidades_proceso(request):
    unidad_id =request.GET.get('unidadId')
    data = {
           'procesos_tipo':listar_procesos_tipo(unidad_id)
        }    
    return render(request, 'Ejecucion/unidades_procesos.html',data)

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

def listar_usuarios_segun_cargo(idcargo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('listar_usuarios_segun_cargo', [out_cursor, idcargo])

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
    cursor.callproc('SP_LISTAR_PROCESOS_TAREAS_TIPO',[out_cursor, idproceso])
   
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
    
#metodos procedimientos almacenados
def recalcular_proceso(id_proceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_RECALCULAR_PROCESO',[id_proceso, salida])
    return salida.getvalue()

def recalcular_tarea(id_proceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_RECALCULAR_PROCESO',[id_proceso, salida])
    return salida.getvalue()

def terminar_tarea(idtarea):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_TERMINAR_TAREA',[idtarea, salida])
    return salida.getvalue()
    
def procesos_tarea(request):
    proceso_id =request.GET.get('procesoid')
    data = {
           'procesos_tarea':listar_procesos_tareas_tipo(proceso_id)
        }
    return render(request, 'Ejecucion/procesos_tareas.html',data)

def procesos_ejecutados(request):
    unidad_id =request.GET.get('unidadid')
    data = {
           'procesos_ejecutados':listar_procesos_ejecutados(unidad_id)
        }
    return render(request, 'Ejecucion/procesos_ejecutados.html',data)
def listar_procesos_tareas_ejecutadas(idproceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_LISTAR_PROCESOS_TAREAS_EJECUTADAS',[out_cursor,idproceso])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def listar_procesos_ejecutados(idproceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_LISTAR_UNIDAD_PROCESOS_EJECUTADOS',[out_cursor,idproceso])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista

def procesos_tarea_ejecutadas(request):
    proceso_e =request.GET.get('procesos_e')
    data = {
           'procesos_tarea_ejecutada':listar_procesos_tareas_ejecutadas(proceso_e)
        }
    return render(request, 'Ejecucion/procesos_tareas_ejecutadas.html',data)

def listar_procesos_tareas_ejecutadas(idproceso):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('SP_LISTAR_PROCESOS_TAREAS_EJECUTADAS',[out_cursor,idproceso])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista