from django.db import models

# Create your models here.

class Persona(models.Model):
	rut = models.CharField(max_length=11, unique=True)
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
