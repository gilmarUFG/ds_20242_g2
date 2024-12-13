from django import forms

from processos.models import Imagem, Processo


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ProcessoForm(forms.ModelForm):
    imagens = MultipleFileField(required=False)

    class Meta:
        model = Processo
        fields = ("endereco", "razao_solicitacao")

    instance: Processo

    def save(self, commit: bool = True) -> Processo:
        processo: Processo = super().save()

        imagens = self.cleaned_data.get("imagens") or []
        for i in imagens:
            imagem = Imagem(imagem=i, processo=processo)
            imagem.save()

        return processo
