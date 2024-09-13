from django.contrib import admin
from .models import Pedido, ItensPedido

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    ...

@admin.register(ItensPedido)
class ItensPedidoAdmin(admin.ModelAdmin):
    ...