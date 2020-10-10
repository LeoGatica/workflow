from django.db import models

# Create your models here.



class Persona(models.Model):
	rut = models.CharField(max_length=11, unique=True)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()


class Cliente(models.Model):
    run_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'

	


