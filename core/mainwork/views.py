from django.shortcuts import render, redirect
from django.db import connection
import cx_Oracle
from django.contrib import messages
from .models import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
	return render(request, 'index.html')


def logged_in(request):

	return render(request, 'menuPrincipal.html')



def empresas(request):
    data = {
        'empresas':listar_empresas()
        }

    return render(request, 'Empresa/listarEmpresa.html', data)


def proceso(request):

    data = {
        'unidades':listar_unidades(),
        'empresas':listar_empresas(),
        'cargos':listar_cargos()
    }
    
    if request.method == 'POST':

        nombre = request.POST.get('nombre_proceso')
        descripcion =  request.POST.get('descripcion')
        unidad = request.POST.get('unidad')

          
        salida = agregar_procesotipo(nombre, descripcion, unidad)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            return redirect(tarea)    
                          
        else:
            data['mensaje'] = 'No se pudo agregar'

    return render(request, 'Procesos/CrearProceso.html', data)


def tarea(request):

    data = {
        'unidades':listar_unidades(),
        'empresas':listar_empresas(),
        'cargos':listar_cargos(),
        'procesos':listar_procesostipo()
    }
    
    if request.method == 'POST':
      
        nombre = request.POST.get('tarea')
        descripcion =  request.POST.get('descripcionTarea')
        dias = request.POST.get('tiempo')
        cargo = request.POST.get('cargo')
        procesotipo = request.POST.get('proceso')
        
        salida = agregar_tareatipo(nombre, descripcion, dias, cargo, procesotipo)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
                               
        else:
            data['mensaje'] = 'No se pudo agregar'

    return render(request, 'Tareas/CrearTareas.html', data)

def unidad(request):

    data = {
        
        'empresas':listar_empresas()
        
    }
    
    if request.method == 'POST':
      
        nombre = request.POST.get('nombre')
        descripcion =  request.POST.get('descripcion')
        empresa = request.POST.get('empresa')
        estado = '1'

        salida = agregar_unidad(nombre, descripcion, estado, empresa)

        print(salida)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            messages.success(request, 'Servicio editado correctamente')
                               
        else:
            data['mensaje'] = 'No se pudo agregar'
            messages.success(request, 'Servicio NO editado correctamente')

    return render(request, 'Unidades/crearUnidad.html', data)
    

def unidades(request):

    data = {
        
        'unidades':listar_unidades_empresa()
        
    }
    

    return render(request, 'Unidades/listarUnidades.html', data)    



def empresa(request):
    data = {
        'regiones':listar_regiones(),
        'comunas':listar_comunas()
       
    }
    

    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre =  request.POST.get('nombre')
        rubro =  request.POST.get('rubro')
        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')
        estado = '1'
        telefono = request.POST.get('telefono')

       
        salida = agregar_empresa(rut, nombre, rubro, comuna, direccion, telefono, correo, estado)
        
        if salida == 1:
            messages.success(request, 'Empresa creada correctamente')
                                 
        else:
            messages.success(request, 'Empresa no creada ')
      
    return render(request, 'Empresa/crearEmpresa.html', data)
	

def usuarios(request):
    data = {
       'usuarios':listar_usuarios()
    }
    

    return render(request, 'Usuarios/ListarUsuarios.html', data)

def listar_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('sp_listar_usuarios', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista    

def listar_empresas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('sp_listar_empresas', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista 

def editarEmpresa(request, idempresa):
    
    

    if request.method == 'GET':
        regiones = listar_regiones()  
        empresa = Empresa.objects.get(idempresa = idempresa)
        comuna = Comuna.objects.get(nombre_comuna = empresa.comuna_idcomuna)
        region = Region.objects.get(nombre = comuna.id_region)
    else:
        rut = request.POST.get('rut')
        nombre =  request.POST.get('nombre')
        rubro =  request.POST.get('rubro')
        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        salida = editar_empresa(idempresa, rut, nombre, rubro, comuna, direccion, telefono, correo)
        
        if salida == 1:
            messages.success(request, 'Empresa Modificada Correctamente')
                                 
        else:
            messages.success(request, 'Empresa no Modificada ')
            
        return redirect('lista_empresa')
        
              
 

    return render(request,'Empresa/crearEmpresa.html', {'empresa':empresa,'comuna':comuna, 'regiones':regiones,  'region':region } )      

def deshabilitarEmpresa(request, idempresa):
 
    empresa = Empresa.objects.get(idempresa = idempresa)
 
    if request.method =='POST':

        salida = deshabilitar_empresa(idempresa)
        
        if salida == 1:
            messages.success(request, 'Empresa deshabilitada correctamente')
                                 
        else:
            messages.success(request, 'Empresa no deshabilitada ')

        return redirect('lista_empresa')
    return render (request, 'Empresa/eliminarEmpresa.html', {'empresa':empresa})    

def listar_unidades():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_unidades_sinfiltro', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista  

def listar_unidades_empresa():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_unidades_empresa', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista      

def listar_procesostipo():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_procesostipo', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista       

def listar_cargos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_cargos', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista      

def listar_regiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_regiones', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista   

def listar_comuna_region(regionid):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_comunas_region', [out_cursor, regionid])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista      

def regiones_comunas(request):
    regionid = request.GET.get('region_id')
 
    data = {
           'region_comuna':listar_comuna_region(regionid)
        }   
     
    return render(request, 'Empresa/regiones_comuna.html',data)    

def listar_comunas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_comunas', [out_cursor])

    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista         



def agregar_empresa(rut, nombre, rubro, comuna, direccion, telefono, correo, estado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_empresa',[rut, nombre, rubro, comuna, direccion, telefono, correo, estado, salida])
    
    return salida.getvalue()

def editar_empresa(idempresa, rut, nombre, rubro, comuna, direccion, telefono, correo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_editar_empresa',[idempresa, rut, nombre, rubro, comuna, direccion, telefono, correo, salida])
    
    return salida.getvalue()

def deshabilitar_empresa(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_deshabilitar_empresa',[id, salida])
    
    return salida.getvalue()



def agregar_procesotipo(nombre, descripcion, unidad):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_procesotipo',[nombre, descripcion, unidad, salida])
    return salida.getvalue()

def agregar_unidad(nombre, descripcion, estado, empresa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_unidad',[nombre, descripcion, estado, empresa, salida])

    return salida.getvalue()


def agregar_tareatipo(nombre, descripcion, dias, cargo, procesotipo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('sp_agregar_tareatipo',[nombre, descripcion, dias, cargo, procesotipo, salida])
    return salida.getvalue()   

def unidades_cargos(request):
    
    unidad_id =request.GET.get('unidad')
    data = {
           'cargos':listar_unidades_cargos(unidad_id)
        }  
        
    return render(request, 'Ejecucion/unidades_cargos.html',data)    


def listar_unidades_cargos(unidad_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()


    cursor.callproc('SP_LISTAR_UNIDADES_CARGOS',[out_cursor, unidad_id])
   
    lista = []
    for fila in out_cursor:
        lista.append(fila)

    return lista     




