from django.db import models
from datetime import datetime

class Actividad(models.Model):
	titulo = models.CharField(max_length=50)
	foto = models.TextField()#mas adelante cambiar por models.ImageField()
	contenido = models.TextField()
	fecha_inicio = models.DateTimeField()
	fecha_de_termino = models.DateTimeField()
	Lugar = models.CharField(max_length=100)
	def __unicode__(self):
		return self.titulo
	

class Proyecto(models.Model):
	titulo = models.CharField(max_length=50)
	nombre_proyecto_url = models.SlugField()
	contenido = models.TextField()
	def __unicode__(self):
		return self.titulo
	
