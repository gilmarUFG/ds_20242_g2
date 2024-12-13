from django.contrib import admin
from django.urls import include, path
from .views import historicoRelatorios, visualizarRelatorio, updateProcesso

urlpatterns = [
    path("relatorios/", historicoRelatorios, name="historico-relatorios"),
    path("relatorios/visualizar/", visualizarRelatorio, name="visualizar-relatorio"),
    path(
        "<int:processoId>/atualizar/",
        updateProcesso,
        name="atualizar-processo",
    ),
]
