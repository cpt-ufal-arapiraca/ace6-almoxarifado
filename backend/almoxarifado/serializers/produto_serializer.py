from rest_framework import serializers
from ..models import Produto

#Produtos

class ProdutoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produto
		fields = '__all__'

