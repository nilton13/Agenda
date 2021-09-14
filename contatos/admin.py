from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome', 'email', 'categoria')
    list_display_links = ('id','nome','sobrenome')



admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)

