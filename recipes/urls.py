from django.urls import path
from recipes.views import home, sobre, login


urlpatterns = [
    path('', login),
    path('home/', home),
    path('sobre/', sobre),
]
