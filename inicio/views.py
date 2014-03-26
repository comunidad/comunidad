from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, response

def inicio(request):
	usuario = request.user
	return render_to_response('inicio/index.html',{'usuario': usuario},context_instance=RequestContext(request))

def nosotros(request):
	usuario = request.user
	return render_to_response('inicio/nosotros.html',{'usuario': usuario},context_instance=RequestContext(request))

def aliados(request):
	usuario = request.user
	return render_to_response('inicio/aliados.html',{'usuario': usuario},context_instance=RequestContext(request))

def contactenos(request):
	usuario = request.user
	return render_to_response('inicio/contactenos.html',{'usuario': usuario},context_instance=RequestContext(request))

def unete(request):
	usuario = request.user
	return render_to_response('inicio/unete.html',{'usuario': usuario},context_instance=RequestContext(request))

def historia(request):
	usuario = request.user
	return render_to_response('inicio/historia.html',{'usuario': usuario},context_instance=RequestContext(request))

