from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from actividades.views import cronograma 
#from django.views.generic.base import RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

admin.autodiscover()

handler500 = 'django.views.defaults.server_error'
handler404 = 'django.views.defaults.page_not_found'
handler403 = 'django.views.defaults.permission_denied'

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'inicio.views.inicio', name='inicio'),
	#url(r'^blog/', 'blog.views.blog', name='blog'),
	url(r'^noticia/', 'noticia.views.noticia', name='noticias'),
	url(r'^', include('inicio.urls')),
	#url(r'^blog/$', include('blog.urls')),
	url(r'^noticia/$', include('noticia.urls')),
	url(r'^cronograma/', 'actividades.views.cronograma', name='cronograma'),
	
	#blog zinnia
	#url(r'^$', RedirectView.as_view(url='/blog/')),
	url(r'^actualidad/', include('zinnia.urls')),
	url(r'^comentarios/', include('django.contrib.comments.urls')),
	url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	#fin blog zinnia

	#calendario scheduler
	#url(r'^$', TemplateView.as_view(template_name="homepage.html"),),
	url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"),),
	url(r'^calendario/', include('schedule.urls')),
	#fin de calendario scheduler
)


sitemaps = {
	'tags': TagSitemap,
	'blog': EntrySitemap,
	'authors': AuthorSitemap,
	'categories': CategorySitemap
}

urlpatterns += patterns(
	'django.contrib.sitemaps.views',
	url(r'^sitemap.xml$', 'index',{'sitemaps': sitemaps}),
	url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',{'sitemaps': sitemaps}),
)

urlpatterns += patterns('',
	url(r'^403/$', 'django.views.defaults.permission_denied'),
	url(r'^404/$', 'django.views.defaults.page_not_found'),
	url(r'^500/$', 'django.views.defaults.server_error'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
		url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
