from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Modulos
from random import randint


def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        if login and senha:
            try:
                usuario = Usuario.objects.get(login=login, senha=senha)
                request.session['usuario_id'] = usuario.id  # Armazena o ID do usuário na sessão
                return redirect('home')  # Redireciona para a view que mostra os módulos
            except Usuario.DoesNotExist:
                return render(request, 'recipes/pages/login.html', {'error_message': 'Login ou senha inválidos'})
    
    # Renderiza o formulário de login para requisições GET
    return render(request, 'recipes/pages/login.html')




def home(request):
    usuario_id = request.session.get('usuario_id')
    
    usuario = Usuario.objects.get(id=usuario_id)
    modulos = usuario.modulos.all()

    return render(request, 'recipes/pages/home.html', context={
    'boxOptions': modulos, 'person' : usuario,
    })

def config(request):
    return render(request, 'recipes/pages/config.html')

def almox(request):
    return render(request, 'recipes/pages/almoxarifado.html')

def alocssala(request):
    return render(request, 'recipes/pages/alocssala.html')
