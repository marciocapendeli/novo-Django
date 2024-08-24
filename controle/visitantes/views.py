from django.shortcuts import render
from visitantes.forms import VisitanteForm


#registro do visitante
def registrar_visitante(request):
    form = VisitanteForm()
    context = {
        "nome_pagina": "Registrar visitante",
        "form": form,
    }
    return render(request, 'registrar_visitante.html', context)

#adicionado
def index(request):
    return render(request, 'index.html') 

