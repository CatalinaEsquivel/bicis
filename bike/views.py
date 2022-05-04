from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bicicleta/index.html')

def bicicletas(request):
    return render(request,'bicicleta/bicicletas.html')

def iniciosesion(request):
    return render(request,'bicicleta/iniciosesion.html')

def registro(request):
    return render(request,'bicicleta/registro.html')