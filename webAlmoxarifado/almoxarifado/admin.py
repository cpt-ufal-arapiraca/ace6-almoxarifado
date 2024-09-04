from django.contrib import admin
from .models import Modulos, Usuario, AcessoModulos

@admin.register(Modulos)
class ModulosAdmin(admin.ModelAdmin):
    ...

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ...

@admin.register(AcessoModulos)
class AcessoModulosAdmin(admin.ModelAdmin):
    ...


