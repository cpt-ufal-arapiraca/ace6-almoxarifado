from almoxarifado.serializers.usuario_serializer import (UserRegisterSerializer, UserLoginSerializer, UserSerializer,
														 ModuleSerializer, AddModuleToUserSerializer)
from ..models import Usuario, Modulos
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..validations import custom_validation
from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound


class UserListView(APIView):
	permission_classes = [permissions.IsAuthenticated]
    
	def get(self, request):
		pedidos = Usuario.objects.all()
		serializer = UserSerializer(pedidos, many=True)
		return Response({'pedidos': serializer.data}, status=status.HTTP_200_OK)

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
	
##
	
class ModuleListView(APIView):
	permission_classes = [permissions.IsAuthenticated]
    
	def get(self, request):
		pedidos = Modulos.objects.all()
		serializer = ModuleSerializer(pedidos, many=True)
		return Response({'modulos': serializer.data}, status=status.HTTP_200_OK)
	
class ModuleCreateView(APIView):
	permission_classes = (permissions.AllowAny,)
	
	def post(self, request, format=None):

		serializer = ModuleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	
class ModuleUpdateView(generics.UpdateAPIView):
    queryset = Modulos.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ModuleDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        # Obtém o ID da query string (por exemplo: ?id=1)
        module_id = request.query_params.get('id', None)

        if module_id is not None:
            try:
                # Obtém o pedido com o ID fornecido e verifica se pertence ao usuário autenticado
                produto = Modulos.objects.get(id=module_id)
                produto.delete()
                return Response({'message': 'Modulo deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
            except Modulos.DoesNotExist:
                raise NotFound('Modulo não encontrado')
        
        return Response({'error': 'ID não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

class AddModuleToUserView(APIView):
	permission_classes = [permissions.IsAuthenticated]
    
	def post(self, request):
		serializer = AddModuleToUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)