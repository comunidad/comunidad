#encoding:utf-8
from django.db import models
#from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib.auth.models import User
#fs = FileSystemStorage(location='/media/photos')

class TagBlog(models.Model):
	name_tag = models.CharField(max_length=15, help_text='Ingrese nombre', verbose_name='Nombre del Tag')
	description_tag = models.TextField(help_text='Ingrese descripcion', verbose_name='Descripcion del Tag')

	def __unicode__(self):
		return self.name_tag

class Articulo(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título del Articulo', unique=True)
	contenido_articulo = models.TextField(help_text='El contenido del articulo', verbose_name='Contenido del Articulo')
	#imagen = models.ImageField(storage=fs, verbose_name='Imagen')
	usuario = models.ForeignKey(User)
	tag_articulo = models.ManyToManyField(TagBlog)
	num_comentarios = models.IntegerField(default=0)
	fecha_publicada = models.DateTimeField()
	#fin_publicacion = models.DateTimeField()
	#fecha_creacion = models.DateTimeField(default=datetime.now)
	#ultima_actualizacion = models.DateTimeField(default=datetime.now)
	def __unicode__(self):
		return self.titulo


class Comentario(models.Model):
	articulo = models.ForeignKey(Articulo)
	texto_comentario = models.TextField(help_text='Tu Comentario', verbose_name='Comentario')
	fecha_publicacion = models.DateTimeField('fecha de publicacion')
	def __unicode__(self):
		return self.texto_comentario


class Respuesta(models.Model):
	comentario = models.ForeignKey(Comentario)
	texto_respuesta = models.TextField(help_text='Tu Respuesta al comentario', verbose_name='Respuesta')
	def __unicode__(self):
		return self.texto_respuesta