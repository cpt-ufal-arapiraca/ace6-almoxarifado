from rest_framework import serializers
from ..models import Pedido, ItensPedido

#Pedidos

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = ItensPedido
        fields = ['id', 'produto', 'produto_nome', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'data', 'status', 'comentarios', 'itens']


##


class ItensForPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItensPedido
        fields = ['id', 'produto', 'quantidade']


class PedidoCreateSerializer(serializers.ModelSerializer):
    itens = ItensForPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'data', 'status', 'comentarios', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItensPedido.objects.create(pedido=pedido, **item_data)
        return pedido