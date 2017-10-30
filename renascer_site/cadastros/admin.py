from django.contrib import admin
# Register your models here.

from .models import * 
admin.site.register(Curso)
admin.site.register(Eletrodomestico)
admin.site.register(MeioComunicacao)
admin.site.register(AnimalDomestico)
admin.site.register(MeioTransporte)
admin.site.register(GrupoComunitario)
admin.site.register(Doenca)
admin.site.register(Familia)
admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(IdadeFilho)
admin.site.register(Visita)
admin.site.register(Aluno_Cursa)
admin.site.register(Familia_eletrodomestico)
admin.site.register(Familia_Animal)
admin.site.register(Familia_Meiocomunicacao)
admin.site.register(Familia_Transporte)
