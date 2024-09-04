
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name="home"),
    path('config/', views.config, name='home-config'),
    path('almox/', views.almox, name='almoxarifado'),
    path('alocssala/', views.alocssala, name='alocssala'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
