# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    idcargo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    unidad_idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='unidad_idunidad')
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cargo'


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Documento(models.Model):
    iddocumento = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    archivo = models.BinaryField()
    idtareaejecutada = models.ForeignKey('Tareaejecutada', models.DO_NOTHING, db_column='idtareaejecutada')
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'documento'


class Empresa(models.Model):
    idempresa = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    razonsocial = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fechacreacion = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    estado = models.FloatField()
    comuna_idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_idcomuna')

    class Meta:
        managed = False
        db_table = 'empresa'
        unique_together = (('idempresa', 'rut'),)


class Estadotarea(models.Model):
    idestadotarea = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadotarea'


class Procesoejecutado(models.Model):
    idprocesoejecutado = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fechaejecucion = models.DateField(blank=True, null=True)
    fechatermino = models.DateField(blank=True, null=True)
    idprocesotipo = models.ForeignKey('Procesotipo', models.DO_NOTHING, db_column='idprocesotipo')

    class Meta:
        managed = False
        db_table = 'procesoejecutado'


class Procesotipo(models.Model):
    idprocesotipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    unidad_idunidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='unidad_idunidad')

    class Meta:
        managed = False
        db_table = 'procesotipo'


class Region(models.Model):
    idregion = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Responsabletarea(models.Model):
    idresponsabletareausuario = models.BigIntegerField(primary_key=True)
    idtareaejecutada = models.ForeignKey('Tareaejecutada', models.DO_NOTHING, db_column='idtareaejecutada')
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idusuario')
    asignador = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'responsabletarea'


class Rol(models.Model):
    idrol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rol'


class Semaforo(models.Model):
    idsemaforo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semaforo'


class Tareaejecutada(models.Model):
    idtareaejecutada = models.BigIntegerField(primary_key=True)
    idprocesoejecutado = models.ForeignKey(Procesoejecutado, models.DO_NOTHING, db_column='idprocesoejecutado')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    avance = models.BigIntegerField(blank=True, null=True)
    duraciondias = models.BigIntegerField(blank=True, null=True)
    estadotarea_idestadotarea = models.ForeignKey(Estadotarea, models.DO_NOTHING, db_column='estadotarea_idestadotarea')
    semaforo_idsemaforo = models.ForeignKey(Semaforo, models.DO_NOTHING, db_column='semaforo_idsemaforo')

    class Meta:
        managed = False
        db_table = 'tareaejecutada'


class Tareatipo(models.Model):
    idtareatipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    duraciondias = models.BigIntegerField(blank=True, null=True)
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idcargo')
    idprocesotipo = models.ForeignKey(Procesotipo, models.DO_NOTHING, db_column='idprocesotipo')

    class Meta:
        managed = False
        db_table = 'tareatipo'


class Unidad(models.Model):
    idunidad = models.BigIntegerField(primary_key=True)
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_idempresa')
    empresa_rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'unidad'


class Usuario(models.Model):
    idusuario = models.BigIntegerField(primary_key=True)
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_idrol')
    cargo_idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_idcargo')
    foto = models.BinaryField(blank=True, null=True)
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50)
    estado = models.FloatField()

    class Meta:
        managed = False
        db_table = 'usuario'
