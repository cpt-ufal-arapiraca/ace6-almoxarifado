from django.db import models


# Create your models here.

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Entregue', 'Entregue'),
        ('Negado', 'Negado'),
    )
    
    usuario = models.ForeignKey('almoxarifado.Usuario', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.nome}'

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('almoxarifado.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.quantidade} de {self.produto.nome} no pedido {self.pedido.id}'