from django.contrib import admin
from django.urls import include, path
from .views import NovoProcessoView, historicoRelatorios, novo_processo, visualizarRelatorio, updateProcesso

urlpatterns = [
    path("relatorios/", historicoRelatorios, name="historico-relatorios"),
    path("relatorios/visualizar/", visualizarRelatorio, name="visualizar-relatorio"),
    path(
        "<int:processoId>/atualizar/",
        updateProcesso,
        name="atualizar-processo",
    ),
    path("novo/", novo_processo, name="novo-processo"),
]
