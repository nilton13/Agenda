from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone', 'email', 'categoria', 'mostrar')
    list_display_links = ('id','nome','sobrenome')
    list_editable = ('telefone', 'mostrar')



admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)

