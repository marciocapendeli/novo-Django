# controle_visitantes/urls.py
from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='usuarios'),
    path('registrar-visitante/', registrar_visitante, name='registrar_visitante'),
    path('', index, name='index'),#adicionado 
    
]
