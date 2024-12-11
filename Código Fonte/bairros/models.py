from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=15, default='s/n')
    complemento = models.CharField(max_length=200, blank=True, null=True)  # Permite que o complemento seja opcional
    observacao = models.CharField(max_length=150, blank=True, null=True)  # Permite que a observação seja opcional

    def __str__(self):
        return f"{self.logradouro}, {self.bairro}, {self.numero}, {self.complemento}, {self.observacao}"