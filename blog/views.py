from django.http import HttpResponse, Http404
from blog.models import Articulo, Comentario, Respuesta
from django.shortcuts import render_to_response
from django.template import RequestContext

import json

def blog(request):
	articulos = Articulo.objects.all()
	return render_to_response('blog/blog.html', {'articulos': articulos}, context_instance=RequestContext(request))


def tagpage(request, tag):
    articulos = Articulo.objects.filter(tags__name=tag)
    return render_to_response("blog/tagpage.html", {"articulos":articulos, "tag":tag})


def home(request):
	articulos = Articulo.objects.all()[:10]
	return render_to_response('blog/blog.html', {'articulos' : articulos})

def crear(request):
	if request.POST:
		form = ArticuloForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/')
	else:
		form = ArticuloForm()
	 
	args = {}
	args.update(csrf(request))
	
	args['form'] = form

	return render_to_response('blog/crear_articulo.html', args)

def articulos(request):
	return render_to_response('blog/blog.html', {'articulos' : Articulo.objects.all() })

def articulo(request, articulo_id):
	articulo = Articulo.objects.get(id=articulo_id)
	return render_to_response('blog/articulo.html', {'articulo' : articulo })

def agregar_comentario(request, articulo_id):
	articulo = Articulo.objects.get(id=articulo_id)

	if request.POST:
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
	
			comentario.fecha_pub = timezone.now()
			comentario.articulo = articulo

			comentario.save()

			return HttpResponseRedirect('/articulos/%s' % articulo_id)
	else:
		form = ComentarioForm()
	 
	args = {}
	args.update(csrf(request))
	
	args['articulo'] = articulo
	args['form'] = form

	return render_to_response('blog/agregar_comentario.html', args)





















#############################
# otras visitas a modificar #
#############################
def cargar_articulo(request, id):
	if request.is_ajax():
		articulo = Articulo.objects.get(pk=id)
		return HttpResponse(
			json.dumps({'titulo': articulo.titulo, 
				'contenido': articulo.contenido_articulo, 
				'usuario': articulo.usuario }),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404

def guardar_articulo(request):
	if request.is_ajax():

		if request.POST['articulo']:
			articulo = Articulo(titulo=request.POST['articulo'])
			articulo.save()

		articulos = Articulo.objects.all().order_by('-id')

		data = list()
		for articulo in articulos:
			data.append({ 'id': articulo.pk, 'titulo': articulo.titulo })

		return HttpResponse(
			json.dumps({ 'articulos': data }),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404

def cargar_comentarios(request, id):
	if request.is_ajax():
		comentarios = Comentario.objects.filter(articulo__id=id).order_by('-id')

		data = list()
		for comentario in comentarios:
			data.append(comentario.texto_comentario)

		return HttpResponse(
			json.dumps({'comentarios': data, 'articulo': id}),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404

def guardar_comentarios(request):
	if request.is_ajax():

		if request.POST['comentario']:
			comentario = Comentario(titulo=request.POST['comentario'], articulo_id=request.POST['articulo'])
			comentario.save()

		return cargar_comentarios(request, request.POST['articulo'])

def cargar_respuestas(request, id):
	if request.is_ajax():
		respuestas = Respuestas.objects.filter(comentario__id=id).order_by('-id')

		data = list()
		for respuesta in respuestas:
			data.append(respuesta.titulo)

		return HttpResponse(
			json.dumps({'respuestas': data, 'comentario': id}),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404

def guardar_respuesta(request):
	if request.is_ajax():

		if request.POST['respuesta']:
			respuesta = Respuestas(titulo=request.POST['respuesta'], comentario_id=request.POST['comentario'])
			respuesta.save()

		return cargar_respuestas(request, request.POST['comentario'])


def cargar_articulo(request, id):
	if request.is_ajax():
		articulo = Articulo.objects.get(pk=id)
		return HttpResponse(
			json.dumps({'titulo': articulo.titulo, 'contenido_articulo': articulo.contenido_articulo, 'usuario': articulo.usuario }),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404