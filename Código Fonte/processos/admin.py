from django.contrib import admin

from processos.models import ParecerTecnico, Processo

# Register your models here.
admin.site.register(Processo)
admin.site.register(ParecerTecnico)
