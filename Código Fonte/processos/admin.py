from django.contrib import admin

from processos.models import ParecerTecnico, Processo

class ProcessoAdmin(admin.ModelAdmin):
    pass

class ParecerTecnicoAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Processo)
admin.site.register(ParecerTecnico)
