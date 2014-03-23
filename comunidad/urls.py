from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from blog.views import *
from actividades.views import cronograma

admin.autodiscover()
urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'inicio.views.inicio', name='inicio'),
	url(r'^blog/', 'blog.views.blog', name='blog'),
	url(r'^noticia/', 'noticia.views.noticia', name='noticias'),
	url(r'^', include('inicio.urls')),
	url(r'^blog/$', include('blog.urls')),
	url(r'^noticia/$', include('noticia.urls')),
	url(r'^cronograma/', 'actividades.views.cronograma', name='cronograma')
	#url(r'^cargar-contenido-articulo/(?P<id>\d+)$', 'blog.views.cargar_articulo', name='cargar_articulo'),
	#url(r'^guardar-articulo/$', 'blog.views.guardar_articulo', name='guardar_articulo'),
	#url(r'^cargar-comentario/(?P<id>\d+)$', 'blog.views.cargar_comentario', name='cargar_comentario'),
	#url(r'^guardar-comentario/$', 'blog.views.guardar_comentario', name='guardar_comentario'),
	#url(r'^cargar-respuestas/(?P<id>\d+)$', 'blog.views.cargar_respuestas', name='cargar_respuestas'),
	#url(r'^guardar-respuesta/$', 'blog.views.guardar_respuesta', name='guardar_respuesta'),
	#url(r'^blog/$', include(blog.urls) ),
)