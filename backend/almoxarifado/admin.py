from django.contrib import admin
from .models import Modulos, Usuario, AcessoModulos, Produto, Log

@admin.register(Modulos)
class ModulosAdmin(admin.ModelAdmin):
    ...

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ...

@admin.register(AcessoModulos)
class AcessoModulosAdmin(admin.ModelAdmin):
    ...

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    ...

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    ...

