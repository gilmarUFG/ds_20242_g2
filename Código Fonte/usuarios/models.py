from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField

from polymorphic.models import PolymorphicModel

# Create your models here.

class Usuario(PolymorphicModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = CPFField()
    data_nascimento = models.DateField()
    endereco = models.TextField(max_length=200)


class Tecnico(Usuario):
    cargo = models.CharField(max_length=100)
    data_admissao = models.DateField()
    matricula = models.CharField(max_length=100)
