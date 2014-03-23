from django.db import models
		
class Curso(models.Model):
	nombre_curso = models.CharField(max_length=30)
	descripcion_curso = models.TextField()

	def __unicode__(self):
		return self.nombre_curso
	