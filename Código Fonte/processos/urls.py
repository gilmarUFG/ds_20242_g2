from django.shortcuts import redirect
from django.urls import path
from .views import (
    MeusProcessosView,
    historicoRelatorios,
    novo_processo,
    visualizarRelatorio,
    updateProcesso,
)

urlpatterns = [
    path("relatorios/", historicoRelatorios, name="historico-relatorios"),
    path("relatorios/visualizar/", visualizarRelatorio, name="visualizar-relatorio"),
    path(
        "<int:processoId>/atualizar/",
        updateProcesso,
        name="atualizar-processo",
    ),
    path("novo/", novo_processo, name="novo-processo"),
    path("meus/", MeusProcessosView.as_view(), name="meus-processos"),
    path("", lambda req: redirect(to="meus-processos")),
]
