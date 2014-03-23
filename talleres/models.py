from django.db import models

# Create your models here.
class Taller(models.Model):
	nombre_taller = models.CharField(max_length=30)
	descripcion_taller = models.TextField()

	def __unicode__(self):
		return self.nombre_taller
	