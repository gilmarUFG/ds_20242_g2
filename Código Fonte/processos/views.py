from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.decorators import login_required

from processos.forms import ProcessoForm
from .models import Processo, Imagem, Documento, ParecerTecnico
from datetime import date, timedelta
import json


def historicoRelatorios(request):
    periodo = request.GET.get("periodo")
    risco = request.GET.get("risco")
    processos = Processo.objects.all()
    if periodo:
        if periodo == "Ultima Semana":
            end_date = date.today()
            start_date = end_date - timedelta(days=7)
            processos = processos.filter(abertura__range=[start_date, end_date])
        elif periodo == "Último mês":
            end_date = date.today()
            start_date = end_date.replace(day=1) - timedelta(days=30)
            processos = processos.filter(abertura__range=[start_date, end_date])
        elif periodo == "Ultimo Semestre":
            end_date = date.today()
            start_date = end_date - timedelta(days=185)
            processos = processos.filter(abertura__range=[start_date, end_date])

    if risco:
        risk_min, risk_max = risco.split("-")
        processos = processos.filter(
            indice_prioridade__gte=float(risk_min),
            indice_prioridade__lte=float(risk_max),
        )

    return render(request, "historico_relatorios.html", {"processos": processos})


def visualizarRelatorio(request):
    processoId = int(request.GET.get("processoId"))
    processo = Processo.objects.get(id=processoId)
    imagens = Imagem.objects.filter(processo=processo).all()
    documentos = Documento.objects.filter(processo=processo).all()
    return render(
        request,
        "visualizar_relatorio.html",
        {
            "processo": processo,
            "imagens": imagens,
            "documentos": documentos,
        },
    )


def updateProcesso(request, processoId):
    novoAndamento = json.loads(request.body.decode("utf-8"))["status"]
    laudo = json.loads(request.body.decode("utf-8"))["laudo"]
    justificativa = json.loads(request.body.decode("utf-8"))["justificativa"]
    recomendacao = json.loads(request.body.decode("utf-8"))["recomendacao"]
    try:
        processo = Processo.objects.get(id=processoId)
        if laudo and justificativa and recomendacao:
            novoParecerTecnico = ParecerTecnico(
                processo=processo,
                laudo=laudo,
                justificativa=justificativa,
                recomendacao=recomendacao,
            )
            novoParecerTecnico.save()
        if novoAndamento in Processo.Status.choices.keys():
            processo.status = novoAndamento
            processo.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    except Processo.DoesNotExist:
        return HttpResponse(status=404)


@login_required
def novo_processo(request: HttpRequest) -> HttpResponse:
    form = ProcessoForm()

    if request.method == "POST":
        form = ProcessoForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.solicitante = request.user.usuario
            form.save()
            # TODO: Redirect to the correct URL
            return redirect("historico-relatorios")

    return render(
        request,
        "novo_processo.html",
        {"form": form},
    )


class NovoProcessoView(CreateView):
    model = Processo
    form_class = ProcessoForm
