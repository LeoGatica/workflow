from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.
def index(request):
	return render(request, 'index.html')


def logged_in(request):

	return render(request, 'menuPrincipal.html')


def empresas(request):
    data = {
        'empresas':listar_empresas()
        }

    return render(request, 'Empresa/listarEmpresa.html')


def empresa(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre =  request.POST.get('nombre')
        rubro =  request.POST.get('rubro')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        salida = agregar_empresa(rut, nombre, rubro, direccion, telefono)
      
           

    return render(request, 'Empresa/crearEmpresa.html')
	

def clientes(request):
    data = {
       'clientes':listar_clientes()
    }
    
    if request.method == 'POST':
        run_id = request.POST.get('run')
        nombre =  request.POST.get('nombre')
        apellido =  request.POST.get('apellido')
        salida = agregar_clientes(run_id, nombre, apellido)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            data['clientes'] =  listar_clientes()
        else:
            data['mensaje'] = 'No se pudo agregar'


    return render(request, 'mainwork/crearCliente.html', data)

def listar_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_CLIENTES', [out_cursor])

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


def agregar_empresa(rut, nombre, rubro, direccion, telefono):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_EMPRESA',[rut, nombre, rubro, direccion, telefono, salida])
    return salida.getvalue()

def agregar_clientes(run,nombre,apellido):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTES',[run, nombre, apellido, salida])
    return salida.getvalue()
	

