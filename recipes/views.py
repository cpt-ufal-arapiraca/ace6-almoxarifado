from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME')

def contato(contato):
    return HttpResponse('contato')

def sobre(sobre):
    return HttpResponse('sobre')
