from django.urls import path
from .views import index, salvar_endereco, enderecos_por_regiao  # Certifique-se de importar a view correta

urlpatterns = [
    path('', index, name='index'),  # URL para a página inicial
    path('consulta-cep/', index, name='consulta_cep'),  # URL para a consulta de CEP
    path('salvar-endereco/', salvar_endereco, name='salvar_endereco'),  # URL para salvar o endereço
    path('enderecos-por-regiao/', enderecos_por_regiao, name='enderecos_por_regiao'),  # URL para endereços por região
]