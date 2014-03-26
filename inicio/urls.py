from django.conf.urls import patterns, include, url
from inicio.views import nosotros, contactenos, unete, aliados, historia

urlpatterns = patterns('',
	url(r'nosotros','inicio.views.nosotros', name='nosotros'),
	url(r'contactenos','inicio.views.contactenos', name='contactenos'),
	url(r'unete','inicio.views.unete', name='unete'),
	url(r'aliados','inicio.views.aliados', name='aliados'),
	url(r'historia','inicio.views.historia', name='historia'),
)