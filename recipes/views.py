from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_person, make_sector


def login(request):
    return render(request, 'recipes/pages/login.html')

def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'person':make_person(),
        'boxOptions':[make_sector() for _ in range(6)],

    })

def config(request):
    return render(request, 'recipes/pages/config.html')
