from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline

from usuarios.models import Tecnico, Usuario


class PerfilInlineFormset(StackedPolymorphicInline.formset):
    def clean(self):
        super().clean()

        if len(self.forms) != 1 or (
            hasattr(self.forms[0], "cleaned_data") and not self.forms[0].cleaned_data
        ):
            raise forms.ValidationError("Você deve ter pelo menos um perfil cadastrado")


class PerfilInline(StackedPolymorphicInline):
    class UsuarioInline(StackedPolymorphicInline.Child):
        model = Usuario

    class TecnicoInline(StackedPolymorphicInline.Child):
        model = Tecnico

    formset = PerfilInlineFormset

    model = Usuario
    child_inlines = (
        UsuarioInline,
        TecnicoInline,
    )
    verbose_name = "Perfil"
    max_num = 1


admin.site.unregister(User)


@admin.register(User)
class UsuarioAdmin(PolymorphicInlineSupportMixin, BaseUserAdmin):
    inlines = [PerfilInline]
