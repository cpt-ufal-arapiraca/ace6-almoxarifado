from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from ..models import Usuario, Modulos, AcessoModulos

UserModel = get_user_model()

#usuario

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(login=clean_data['login'], password=clean_data['password'])
		user_obj.login = clean_data['login']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	login = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(login=clean_data['login'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user
	
class AddModuleToUserSerializer(serializers.Serializer):
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    modulo_id = serializers.PrimaryKeyRelatedField(queryset=Modulos.objects.all())

    def create(self, validated_data):
        usuario = validated_data['usuario_id']
        modulo = validated_data['modulo_id']
        
        # Cria uma nova associação
        acesso_modulo, created = AcessoModulos.objects.get_or_create(usuario=usuario, modulo=modulo)
        return acesso_modulo

class ModuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Modulos
		fields = '__all__'

class ModuleForUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Modulos
		fields = ('id','nome')

class UserSerializer(serializers.ModelSerializer):
	modulos = serializers.SerializerMethodField()

	class Meta:
		model = Usuario
		fields = ('id','nome', 'login','last_login','email','is_active','is_staff','modulos')

	def get_modulos(self, obj):
		acessos = AcessoModulos.objects.filter(usuario=obj)
		modulos = [acesso.modulo for acesso in acessos]
		return ModuleForUserSerializer(modulos, many=True).data