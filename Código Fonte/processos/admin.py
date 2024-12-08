from django.contrib import admin

from processos.models import ParecerTecnico, Processo, Imagem, Documento
from usuarios.models import Tecnico,Usuario

# Register your models here.
admin.site.register(Processo)
admin.site.register(ParecerTecnico)
admin.site.register(Imagem)
admin.site.register(Documento)
admin.site.register(Tecnico)
admin.site.register(Usuario)
