#encoding:utf-8
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TagNoticia(models.Model):
	name_tag = models.CharField(max_length=15, help_text='Ingrese nombre', verbose_name='Nombre del Tag')
	description_tag = models.TextField(help_text='Ingrese descripcion', verbose_name='Descripcion del Tag')

	def __unicode__(self):
		return self.name_tag


class Noticia(models.Model):
	titulo = models.CharField(max_length=40, verbose_name='Título de la Noticia', unique=True)
	descripcion_noticia = models.CharField(max_length=100, help_text='Dispone de 100 caracteres para su descripcion de la noticia')
	url_noticia = models.URLField()
	usuario = models.ForeignKey(User)
	tag_noticia = models.ManyToManyField(TagNoticia)
	num_comentarios = models.IntegerField(default=0)
	fecha_publicada = models.DateTimeField()
	def __unicode__(self):
		return self.titulo


class ComentarioNoticia(models.Model):
	noticia = models.ForeignKey(Noticia)
	comentario_noticia = models.TextField(help_text='Tu Comentario', verbose_name='Comentario')
	fecha_publicacion = models.DateField('fecha de publicacion')
	hora_publicacion = models.TimeField('hora de publicacion')
	def __unicode__(self):
		return self.comentario_noticia
		


class RespuestaNoticia(models.Model):
	comentario = models.ForeignKey(ComentarioNoticia)
	texto_respuesta = models.TextField(help_text='Tu Respuesta al comentario de una noticia', verbose_name='Respuesta')
	def __unicode__(self):
		return self.texto_respuesta
