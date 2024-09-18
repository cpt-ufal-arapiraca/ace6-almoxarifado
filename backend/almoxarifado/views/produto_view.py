from almoxarifado.serializers.produto_serializer import (ProdutoSerializer)
from ..models import Produto, ItensPedido
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class ProdutoListView(APIView):
	permission_classes = [permissions.IsAuthenticated]
    
	def get(self, request):
		produto = Produto.objects.all()
		serializer = ProdutoSerializer(produto, many=True)
		return Response({'produtos': serializer.data}, status=status.HTTP_200_OK)
	
class ProdutoCreateView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, request, format=None):
		serializer = ProdutoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class ProdutoDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        # Obtém o ID da query string (por exemplo: ?id=1)
        produto_id = request.query_params.get('id', None)

        if produto_id is not None:
            try:
                # Obtém o pedido com o ID fornecido e verifica se pertence ao usuário autenticado
                produto = Produto.objects.get(id=produto_id, usuario=request.user)
                produto.delete()
                return Response({'message': 'Pedido deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
            except Produto.DoesNotExist:
                raise NotFound('Pedido não encontrado ou não pertence ao usuário')
        
        return Response({'error': 'ID não fornecido'}, status=status.HTTP_400_BAD_REQUEST)
    
class ProdutoUpdateView(generics.UpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class ProdutoByNameView(generics.ListAPIView):
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)  # Busca o parâmetro "nome" da URL
        if nome:
            # Retorna produtos cujo nome contenha a string de busca (case-insensitive)
            return Produto.objects.filter(nome__icontains=nome)
        return Produto.objects.none()