from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class Modulos(models.Model):
    nome = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="recipes/images/modulos")
    link = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="Descrição padrão")

    def __str__(self):
        return self.nome

class UsuarioManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('O campo login deve ser preenchido')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(login, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255, default='Nome Padrão')
    email = models.EmailField(blank=True)
    icon = models.ImageField(upload_to="recipes/images/usuarios", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    modulos = models.ManyToManyField(Modulos, through='AcessoModulos', related_name="usuarios")

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    def __str__(self):
        return self.login

class AcessoModulos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE)


    
    class Meta:
        unique_together = ('usuario', 'modulo')


#almoxarifado


class Produto(models.Model):
    MEDIDA_CHOICES = (
        ('Caixa', 'Caixa'),
        ('Unidade', 'Unidade'),
    )

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    estoque = models.IntegerField()
    medida = models.CharField(max_length=20, choices=MEDIDA_CHOICES, default='Unidade')
    minimo = models.IntegerField(default=0)
    ifcaixaqtd = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome


    
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
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey('almoxarifado.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.quantidade} de {self.produto.nome} no pedido {self.pedido.id}'
