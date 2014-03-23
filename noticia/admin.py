from django.contrib import admin
from noticia.models import TagNoticia, Noticia, ComentarioNoticia, RespuestaNoticia

admin.site.register(TagNoticia)
admin.site.register(Noticia)
admin.site.register(ComentarioNoticia)
admin.site.register(RespuestaNoticia)
