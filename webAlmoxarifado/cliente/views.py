from django.shortcuts import render

# Create your views here.

def cliente(request):
    return render(request, 'recipes/pages/cliente.html')