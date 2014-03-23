from django.shortcuts import render_to_response
from django.template import RequestContext
from actividades.models import Actividad
# Create your views here.
#def blog(request):
#	articulos = Articulo.objects.all()
#	return render_to_response('blog/blog.html', 
#		{'articulos': articulos}, context_instance=RequestContext(request))

def cronograma(request):
	usuario = request.user
	actividades = Actividad.objects.all()
	return render_to_response('actividades/cronograma.html',
		{'usuario': usuario, 'actividades': actividades},context_instance=RequestContext(request))