from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from usuarios.models import Tecnico, Usuario


class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name = "Perfil"
    verbose_name_plural = "Perfil"
    min_num = 1
    max_num = 1


class TecnicoInline(admin.StackedInline):
    model = Tecnico
    can_delete = False
    verbose_name_plural = "tecnicos"


class UserAdmin(BaseUserAdmin):
    inlines = [UsuarioInline, TecnicoInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
