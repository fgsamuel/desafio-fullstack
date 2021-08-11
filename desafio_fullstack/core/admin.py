from django.contrib import admin

from desafio_fullstack.core.forms import EstadoForm, CidadeForm
from desafio_fullstack.core.models import Estado, Cidade


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    form = EstadoForm
    search_fields = ('sigla', 'nome')


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_estado')
    form = CidadeForm
    search_fields = ('nome', 'estado__nome')

    def get_estado(self, obj):
        return obj.estado.nome

    get_estado.short_description = 'Estado'


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
