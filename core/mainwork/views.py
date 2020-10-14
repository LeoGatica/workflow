from django.shortcuts import render, redirect
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

        print(nombre)
        print(descripcion)
        print(empresa)
        print(estado)
        
        salida = agregar_unidad(nombre, descripcion, estado, empresa)

        print(salida)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
                               
        else:
            data['mensaje'] = 'No se pudo agregar'

    return render(request, 'Unidades/crearUnidad.html', data)
    

def unidades(request):

    data = {
        
        'unidades':listar_unidades()
        
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
            data['mensaje'] = 'Agregado correctamente'
                               
        else:
            data['mensaje'] = 'No se pudo agregar'
      
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

def listar_unidades():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc('sp_listar_unidades_sinfiltro', [out_cursor])

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
    print(salida)
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


