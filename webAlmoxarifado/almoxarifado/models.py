from django.db import models


# Create your models here.
class Modulos(models.Model):
    nome = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="recipes/images/modulos")
    link = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="recipes/images/usuarios", null=True)
    modulos = models.ManyToManyField('Modulos', through='AcessoModulos', related_name='usuarios')

    def __str__(self):
        return self.nome

class AcessoModulos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE)


    
    class Meta:
        unique_together = ('usuario', 'modulo')