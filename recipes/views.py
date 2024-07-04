from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'recipes/login.html')

def home(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return HttpResponse('sobre')
