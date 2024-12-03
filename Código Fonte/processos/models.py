from django.db import models

from usuarios.models import Tecnico, Usuario

# Create your models here.


class Processo(models.Model):
    class Status:
        ABERTO = 'ABERTO'
        EM_ANALISE = 'EM_ANALISE'
        CANCELADO = 'CANCELADO'
        ENCERRADO = 'ENCERRADO'
        ENCAMINHADO = 'ENCAMINHADO'

        choices = {
            ABERTO: 'Aberto',
            EM_ANALISE: 'Em Análise',
            CANCELADO: 'Cancelado',
            ENCERRADO: 'Encerrado',
            ENCAMINHADO: 'Encaminhado'
        }

    class Situacao:
        SAUDAVEL = 'SAUDAVEL'
        DOENTE = 'DOENTE'
        choices = {
            SAUDAVEL: 'Saudável',
            DOENTE: 'Doente',
        }

    tecnico_responsavel = models.ForeignKey(Tecnico, on_delete=models.PROTECT, null=True, blank=True, related_name='processo_responsavel')
    solicitante = models.ForeignKey(Usuario, related_name='processo_solicitante', on_delete=models.CASCADE)

    endereco = models.TextField(max_length=200)
    razao_solicitacao = models.TextField(max_length=1000)
    indice_prioridade = models.FloatField()
    status = models.CharField(choices=Status.choices, default=Status.ABERTO, max_length=30)
    situacao = models.CharField(choices=Situacao.choices, null=True, blank=True, max_length=30)

    abertura = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)

class ParecerTecnico(models.Model):
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)

    laudo = models.TextField(max_length=1000)
    justificativa = models.TextField(max_length=1000)
    recomendacao = models.TextField(max_length=1000)

class Imagem(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='pareceres/imagens/')

class Documento(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='pareceres/imagens/')

