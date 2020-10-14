from django.db import models

# Create your models here.

class Cliente(models.Model):
    run_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):        
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    email = models.EmailField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    telefono =  models.IntegerField()
    estado = models.BooleanField(('Estado'), default=True)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estado = models.BooleanField(('Estado'), default=True)

    def __str__(self):
        return self.nombre




class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    estado = models.BooleanField(('Estado'), default=True)

    def __str__(self):
        return self.nombre


class ProcesoTipo(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TareaTipo(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    duracion_dias = models.IntegerField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    procesotipo = models.ForeignKey(ProcesoTipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


	


