from django.contrib import admin
from .models import Modulos, Usuario, AcessoModulos, Produto, Pedido, ItensPedido

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

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    ...

@admin.register(ItensPedido)
class ItensPedidoAdmin(admin.ModelAdmin):
    ...