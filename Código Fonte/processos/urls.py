from django.contrib import admin
from django.urls import include, path
from .views import historicoRelatorios,visualizarRelatorio,updateProcesso

urlpatterns = [
    path('historico-relatorios/',historicoRelatorios,name='historico-relatorios'),
    path('visualizar-relatorio/',visualizarRelatorio,name='visualizar-relatorio'),
    path('atualizar-processo/<int:processoId>/',updateProcesso,name='atualizar-processo'),
]
