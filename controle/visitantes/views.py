from django.shortcuts import render



#registro do visitante
def registrar_visitante(request):
    return render(request, 'registrar_visitante.html')

#adicionado
def index(request):
    return render(request, 'index.html')