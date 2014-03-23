from django.shortcuts import render_to_response
from django.template import RequestContext

from noticia.models import Noticia

def noticia(request):
	noticias = Noticia.objects.all()
	return render_to_response('noticia/noticia.html', 
		{'noticias': noticias}, context_instance=RequestContext(request))


