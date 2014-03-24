from blog.models import Articulo, Comentario, Respuesta, TagBlog
from django.contrib import admin

#from actions import export_as_csv

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('id','titulo', 'contenido_articulo', 'usuario', 'num_comentarios')
	list_filter = ('usuario',)
	search_fields = ('categoria__titulo', 'usuario__email')
	#list_editable = ('titulo',)
	#list_display_links = ('es_popular',)
	#actions = [export_as_csv]
	#raw_id_fields = ('tag', 'usuario')

	def imagen_num_comentarios(self, obj):
		url = obj.mis_num_comentarios()
		tag = '<img src="%s">' % url
		return tag
	imagen_num_comentarios.allow_tags = True
	imagen_num_comentarios.admin_order_field = 'num_comentarios'

class ArticuloInline(admin.StackedInline):
	model = Articulo
	extra = 3
	raw_id_fields = ('usuario',)


class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('id','texto_comentario',)
	#filter_vertical = ('articulo',)


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario)
admin.site.register(Respuesta)
admin.site.register(TagBlog)




