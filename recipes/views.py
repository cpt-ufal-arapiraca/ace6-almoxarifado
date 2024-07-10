from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'recipes/pages/login.html')

def home(request):
    return render(request, 'recipes/pages/home.html')

def config(request):
    return render(request, 'recipes/pages/config.html')
