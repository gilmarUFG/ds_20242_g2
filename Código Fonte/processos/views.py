from django.shortcuts import render
from .models import Processo

# Create your views here.
def historicoRelatorios(request):
  processos = Processo.objects.all()
  print(processos)

  return render(request, 'historico_relatorios.html',{'processos':processos})