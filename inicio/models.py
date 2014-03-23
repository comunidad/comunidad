from django.db import models
#frase del dia a compartir en redes sociales
STATUS = [
	('uno','escolar'),
	('dos','Academico'),
	('tres','universitario'),
	('cuatro','otro'),
]

class Frase(models.Model):
	frase = models.CharField(max_length=150)
	autor = models.CharField(max_length=50)
	fecha_de_publicacion = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.frase

#poesia del dia a compartir en redes sociales
class Poesia(models.Model):
	poesia = models.TextField()
	autor = models.CharField(max_length=50)
	fecha_de_publicacion = models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.poesia

#organizaciones aliadas
class OrgAliados(models.Model):
	nombre = models.CharField(max_length=50)
	acerca_de_org = models.TextField()
	#intereses = models.ManyToManyField(TagBlog)
	def __unicode__(self):
		return self.nombre

class Miembros(models.Model):
	nombre = models.CharField(max_length=50)
	estado_actual = models.CharField(max_length=15, choices=STATUS, default='cuatro')
	lugar_de_estudio = models.CharField(max_length=50)
	distrito = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre    
