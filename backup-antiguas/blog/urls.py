from django.conf.urls import patterns, include, url

from blog.views import articulo

urlpatterns = patterns('',
	url(r'^articulo/(?P<id>\d+)$', 'blog.views.articulo', name='articulo'),
	url(r'^todos/$', 'blog.views.articulos'),
	url(r'^obtener/(?P<articulo_id>\d+)/$', 'blog.views.articulo'),
	url(r'^agregar_comentario/(?P<articulo_id>\d+)/$', 'blog.views.agregar_comentario'),
)